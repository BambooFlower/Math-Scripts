package fortuna

import (
	"testing"
)

// TestSynchronizedGenerator tests that a syncronized Fortuna PRNG does not
// generate random series which overlap when used in 2 goroutines.
func TestSynchronizedGenerator(t *testing.T) {
	prng := NewSynchronizedGenerator()
	testSyncronization(t, prng)
}

func testSyncronization(t *testing.T, prng PRNG) {
	x := make([]int64, 5000)
	y := make([]int64, 5000)
	c1 := make(chan bool)
	c2 := make(chan bool)
	go newRandoms(prng, x, c1)
	go newRandoms(prng, y, c2)
	<-c1
	<-c2
	for i, xi := range x {
		for j, yj := range y {
			if xi == yj {
				t.Errorf("PRNG.Int63, found an overlap x[#%d], y[%d]: %d, %d", i, j, xi, yj)
				break
			}
		}
	}
}

func newRandoms(prng PRNG, x []int64, ch chan<- bool) {
	for i := range x {
		x[i] = prng.Int63()
	}
	ch <- true
}
