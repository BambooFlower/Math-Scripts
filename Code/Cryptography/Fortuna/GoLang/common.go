package fortuna

import (
	"hash"
	"log"
	"strconv"
	"time"
)

var _DEBUG bool = false
var _DEBUGLEVEL = 4

func logTrace(msg string) {
	if _DEBUG && _DEBUGLEVEL > 5 {
		logLog("TRACE", msg)
	}
}

func logDebug(msg string) {
	if _DEBUG && _DEBUGLEVEL > 4 {
		logLog("DEBUG", msg)
	}
}

func logInfo(msg string) {
	if _DEBUG && _DEBUGLEVEL > 3 {
		logLog("INFO ", msg)
	}
}

func logWarn(msg string) {
	if _DEBUG && _DEBUGLEVEL > 2 {
		logLog("WARN ", msg)
	}
}

func logError(msg string) {
	if _DEBUG && _DEBUGLEVEL > 1 {
		logLog("ERROR", msg)
	}
}

func logFatal(msg string) {
	if _DEBUG && _DEBUGLEVEL > 0 {
		logLog("FATAL", msg)
	}
}

func logLog(cat, msg string) {
	if _DEBUG {
		log.Print(cat + " - " + msg)
	}
}

type SeedingError struct {
	Msg string
}

func (e SeedingError) Error() string { return "crypto/fortuna: " + e.Msg }

// currentTimeMillis returns the current time in milliseconds since the Unix
// epoch.
func currentTimeMillis() int64 {
	result := time.Now().UnixNano()
	return result / 1e6
}

// isZero returns false if any of the bytes in buffer is not 0. It returns
// true otherwise.
func isZero(buffer []byte) bool {
	for i := range buffer {
		if buffer[i] != 0 {
			return false
		}
	}
	return true
}

// int63 returns a non-negative pseudo-random 63-bit integer as an int64.
func int63(prng PRNG) int64 {
	buffer := make([]byte, 8)
	n, _ := prng.Read(buffer)
	if n != 8 {
		logError("int63(): Was expecting 8 bytes but got " + strconv.Itoa(n))
		panic("oops: not enough random bytes are available\n")
	}
	result := int64((buffer[0] & 0x7F) << 56)
	for i := 0; i < 7; i++ {
		result |= int64(buffer[1+i]) << uint(48-8*i)
	}
	return result
}

// increment increments in-situ the unpacked integer assumed to be in network
// byte order.
func increment(counter []byte) {
	for i := len(counter) - 1; i >= 0; i-- {
		counter[i]++
		if counter[i] != 0 {
			break
		}
	}
}

// toBytes unpacks and returns an 8-byte array from the given integer n.  The
// returned bytes are arranged in network (Big endian) order with the Most
// Significant Byte at index 0.
func toBytes(n int64) []byte {
	result := make([]byte, 8)
	for i := 0; i < 8; i++ {
		result[i] = byte(n >> uint(56-(8*i)))
	}
	return result
}

func toString(es entropySource) string { return "source #" + strconv.Itoa(es.getID()) }

func updateHash(b byte, md hash.Hash) {
	buffer := make([]byte, 1)
	buffer[0] = b
	md.Write(buffer)
}
