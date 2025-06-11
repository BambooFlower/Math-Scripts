package fortuna

import (
	aes "crypto/aes"
	"crypto/cipher"
	sha "crypto/sha256"
	"hash"
	"time"
)

// Maximum number of bytes to return per one Read request.
var maxBytesPerRequest int = 1 << 20

// The Fortuna Generator.
// On its own it is also a cryptographically strong pseudorandom number
// generator base on an AES in Counter mode.
type Generator struct {
	// IMPLEMENTATION NOTE (rsn) - we replicate the structure and functions
	// found in crypto/block/ctr.go here because: (a) we need access to the
	// key-stream of the cipher running in counter mode, and (b) we need to
	// re-key the cipher without altering the value of the counter.  While we
	// could've addressed the 1st issue by making the newCTRStream function in
	// that file public we would still have a problem addressing the 2nd issue.
	aes     cipher.Block
	key     []byte    // a 256-bit key initialized to 0
	counter []byte    // a 16-byte (AES block size) counter starting at 0
	tmp     []byte    // temp buffer to hold up to 128-bit of keystream data
	md      hash.Hash // a SHA-256 instance for re-seeding purposes
}

// NewGenerator conveniently calls NewSeededGenerator passing the number
// of nanoseconds since the Unix epoch as a seed value via time.Now().UnixNano().
func NewGenerator() *Generator { return NewSeededGenerator(time.Now().UnixNano()) }

// NewSeededGenerator creates, seeds, and returns a Generator.
func NewSeededGenerator(seed int64) *Generator {
	result := NewUnseededGenerator()
	result.Seed(seed)
	return result
}

// NewUnseededGenerator creates, and returns a Generator which needs to be
// seeded before it can be used.
func NewUnseededGenerator() *Generator {
	result := new(Generator)
	result.key = make([]byte, 32)
	result.counter = make([]byte, aes.BlockSize)
	result.md = sha.New()
	result.md.Write(result.key)
	return result
}

// Seed uses the provided seed value to initialize the generator to a
// deterministic state.
// It is also the implementation of the 1st method in rand.Source interface.
func (g *Generator) Seed(seed int64) {
	sb := toBytes(seed)
	g.md.Write(sb)
	g.reseed()
}

// reseed sets up an AES in Counter mode using the current context of the
// Generator's message digest algorithm.
// Formally reseed is specified as:
//
//	K <-- SHA-256(K || s)
//
// We break this operation into two:
// (a) the SHA-256(K) which we do when we first create a new Generator, and
//
//	every time we re-key it, and
//
// (b) the SHA-256(s) which will make sure to call before this method.
// We do this to facilitate the implementation of the Fortuna PRNG reseed
func (g *Generator) reseed() {
	g.key = g.md.Sum(nil)
	c, err := aes.NewCipher(g.key)
	if err != nil {
		m := "G.reseed(): AES error: " + err.Error()
		logFatal(m)
		panic(m + "\n")
	}
	g.aes = c
	increment(g.counter)
}

// Int63 returns a non-negative pseudo-random 63-bit long integer as an int64.
// It is also the implementation of the 2nd method in rand.Source interface.
func (g *Generator) Int63() int64 { return int63(g) }

// Read reads up to len(buffer) bytes into buffer.
// It implements the io.Reader interface with three noticeable differences:
// 1. Read calls will block until enough data is available to fill buffer,
// 2. Read will always return len(buffer) and nil, unless...
// 3. Read will return -1 and an error iff the Generator is not yet seeded.
func (g *Generator) Read(buffer []byte) (n int, err error) {
	if isZero(g.counter) {
		m := "Generator not seeded yet"
		logError("G.Read(): " + m)
		return 0, SeedingError{m}
	}
	limit := len(buffer)
	result := 0
	for limit > 0 {
		x := g.generateBlock(buffer[result:])
		result += x
		limit -= x
		// ...we limit the maximum size of any one request to 2**16 blocks
		// that is 2**20 bytes.
		if result > maxBytesPerRequest && limit > 0 {
			g.rekey()
		}
	}
	// ...after every request we generate an extra 256 bits of pseudorandom
	// data and use that as the new key for the block cipher.
	g.rekey()
	return result, nil
}

// rekey generate new 256 bits of key material and re-key the AES.
// We DO NOT alter the counter though since as the Fortuna designers point out:
// rolling 2**128 bits counter is beyond the computational capabilities of
// today's computers.
func (g *Generator) rekey() {
	g.generateBlock(g.key[0:])
	g.generateBlock(g.key[aes.BlockSize:])
	c, err := aes.NewCipher(g.key)
	if err != nil {
		logError("rekey(): Unexpected AES error: " + err.Error())
		panic("oops: unexpected error while rekeying a Generator: " + err.Error() + "\n")
	}
	g.aes = c
	g.md.Write(g.key)
}

// generateBlock encrypts the Counter into out and increments the Counter.
// if out is shorter than the AES block size, a temporary buffer is created
// and used.  Either way, it returns the actual number of bytes processed in
// out.
func (g *Generator) generateBlock(out []byte) int {
	var result int
	if len(out) < aes.BlockSize {
		result = len(out)
		tmp := make([]byte, aes.BlockSize)
		g.aes.Encrypt(g.counter, tmp)
		copy(out, tmp[0:result])
	} else {
		result = aes.BlockSize
		g.aes.Encrypt(g.counter, out)
	}
	increment(g.counter)
	return result
}

// Compile-time assertion that Generator implements PRNG
var _ PRNG = (*Generator)(nil)
