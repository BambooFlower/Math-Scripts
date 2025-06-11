package fortuna

import (
	"sync"
)

// SynchronizedPRNG is a thread-safe PRNG which can be used with multiple
// goroutines.
type SynchronizedPRNG struct {
	lock sync.Mutex
	prng PRNG
}

// we don't want everybody to call this
func newSynchronizedFortuna(f *Fortuna) *SynchronizedPRNG {
	result := new(SynchronizedPRNG)
	//	result.prng = newFortuna()
	result.prng = f
	return result
}

// it's ok for this to be public
func NewSynchronizedGenerator() *SynchronizedPRNG {
	result := new(SynchronizedPRNG)
	result.prng = NewGenerator()
	return result
}

func (sg *SynchronizedPRNG) Seed(seed int64) {
	sg.lock.Lock()
	sg.prng.Seed(seed)
	sg.lock.Unlock()
}

func (sg *SynchronizedPRNG) Int63() int64 { return int63(sg) }

func (sg *SynchronizedPRNG) Read(buffer []byte) (n int, err error) {
	sg.lock.Lock()
	defer sg.lock.Unlock()
	return sg.prng.Read(buffer)
}

// Compile-time assertion
var _ PRNG = (*SynchronizedPRNG)(nil)
