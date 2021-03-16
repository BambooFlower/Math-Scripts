
package fortuna

import (
	"testing"
	"time"
)

// TestGenerator_1 tests that 2 consecutive random numbers are not equal.
func TestGenerator_1(t *testing.T) {
	prng := NewGenerator()
	v_ := prng.Int63()
	for i := 0; i < 1000; i++ {
		v := prng.Int63()
		if v == v_ {
			t.Errorf("Generator.Int63, 2 consecutive 63-bit values are equal at iter #%d: %d", i, v)
			break
		}
	}
}

// TestGenerator_N tests that a randomly generated number was not among the last
// generated 100 ones.
func TestGenerator_N(t *testing.T) {
	prng := NewGenerator()
	// generate the first 100 randoms
	ring := make([]int64, 100)
	for i := 0; i < 100; i++ {
		ring[i] = prng.Int63()
	}
	n := 0
	for i := 100; i < 1000; i++ {
		v := prng.Int63()
		for i := 0; i < 100; i++ {
			if v == ring[i] {
				t.Errorf("Generator.Int63, a 63-bit value is equal to one already generated previosuly at iter #%d: %d", i, v)
				break
			}
		}
		n++
		n %= 100
		ring[n] = v
	}
}

// TestSeed tests that 2 PRNGs seeded with the same value generate the same
// series of random numbers.
func TestSeed(t *testing.T) {
	prng1 := NewUnseededGenerator()
	prng2 := NewUnseededGenerator()
	seed := time.Nanoseconds()
	prng1.Seed(seed)
	prng2.Seed(seed)
	for i := 0; i < 1000; i++ {
		v1 := prng1.Int63()
		v2 := prng2.Int63()
		if v1 != v2 {
			t.Errorf("Generator.Int63, 2 63-bit values from 2 PRNGs seeded similarly, at iter #%d, are different: #%d: %d", i, v1, v2)
			break
		}
	}
}
