
package fortuna

import (
	"rand"
)

var globalRand = rand.New(globalSyncronizedFortuna)

// Seed uses the provided seed value to initialize the generator to a deterministic state.
func Seed(seed int64) { globalRand.Seed(seed) }

// Int63 returns a non-negative pseudo-random 63-bit integer as an int64.
func Int63() int64 { return globalRand.Int63() }

// Uint32 returns a pseudo-random 32-bit value as a uint32.
func Uint32() uint32 { return globalRand.Uint32() }

// Int31 returns a non-negative pseudo-random 31-bit integer as an int32.
func Int31() int32 { return globalRand.Int31() }

// Int returns a non-negative pseudo-random int.
func Int() int { return globalRand.Int() }

// Int63n returns, as an int64, a non-negative pseudo-random number in [0,n).
func Int63n(n int64) int64 { return globalRand.Int63n(n) }

// Int31n returns, as an int32, a non-negative pseudo-random number in [0,n).
func Int31n(n int32) int32 { return globalRand.Int31n(n) }

// Intn returns, as an int, a non-negative pseudo-random number in [0,n).
func Intn(n int) int { return globalRand.Intn(n) }

// Float64 returns, as a float64, a pseudo-random number in [0.0,1.0).
func Float64() float64 { return globalRand.Float64() }

// Float32 returns, as a float32, a pseudo-random number in [0.0,1.0).
func Float32() float32 { return globalRand.Float32() }

// Perm returns, as a slice of n ints, a pseudo-random permutation of the integers [0,n).
func Perm(n int) []int { return globalRand.Perm(n) }

// NormFloat64 returns a normally distributed float64 in the range
// [-math.MaxFloat64, +math.MaxFloat64] with
// standard normal distribution (mean = 0, stddev = 1).
// To produce a different normal distribution, callers can
// adjust the output using:
//
//  sample = NormFloat64() * desiredStdDev + desiredMean
//
func NormFloat64() float64 { return globalRand.NormFloat64() }

// ExpFloat64 returns an exponentially distributed float64 in the range
// (0, +math.MaxFloat64] with an exponential distribution whose rate parameter
// (lambda) is 1 and whose mean is 1/lambda (1).
// To produce a distribution with a different rate parameter,
// callers can adjust the output using:
//
//  sample = ExpFloat64() / desiredRateParameter
//
func ExpFloat64() float64 { return globalRand.ExpFloat64() }
