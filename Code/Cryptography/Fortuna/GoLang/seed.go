package fortuna

import (
	"os"
	"strconv"
	"time"
)

// Number of times Fortuna is seeded before we update its random seed file.
var timesSeededPeriod = uint64(100)

// writeSeedFile writes Fortuna's random seed to a file in the User's home
// folder.
func writeSeedFile(prng *Fortuna) bool {
	logTrace("--> writeSeedFile()")
	f, e1 := openSeedFile(os.O_WRONLY)
	if e1 != nil {
		logError("writeSeedFile(): Failed opening random seed file: " + e1.Error())
		return false
	}

	defer f.Close()

	buffer := make([]byte, 64)
	_, e2 := prng.Read(buffer)
	if e2 != nil {
		logError("writeSeedFile(): Failed obtaining random seed data: " + e2.Error())
		return false
	}

	_, e3 := f.Write(buffer)
	if e3 != nil {
		logError("writeSeedFile(): Failed writing to random seed file: " + e3.Error())
		return false
	}

	logInfo("writeSeedFile(): Updated random seed file...")
	logTrace("<-- writeSeedFile()")
	return true
}

// updateSeedFile reads Fortuna's random seed from a file in the User's home
// folder, re-seeds the Fortuna's Generator with the value of this seed and
// writes a new seed to the same file.
func updateSeedFile(prng *Fortuna) bool {
	logTrace("--> updateSeedFile()")
	result := false // expect the worse
	f, e1 := openSeedFile(os.O_RDWR)
	if e1 != nil {
		// if it was never there before we need to create it but since we
		// also have to read it before updating it we need a bootstrap
		// procedure.
		if prng.timesSeeded == timesSeededPeriod {
			// by this time we know the file (likely) does not exist but we
			// have enough random state to initialize it.
			logInfo("updateSeedFile(): About to create random seed file")
			e11 := createSeedFile()
			if e11 != nil {
				logError("updateSeedFile(): Failed creating random seed file: " + e11.Error())
			} else {
				result = writeSeedFile(prng)
			}
		} else {
			logError("updateSeedFile(): Failed opening random seed file: " + e1.Error())
		}
	} else {
		s := make([]byte, 128)
		n, e2 := f.Read(s)
		if e2 != nil {
			logError("updateSeedFile(): Failed reading random seed file: " + e2.Error())
			f.Close()
		} else {
			if n != 64 {
				logError("updateSeedFile(): Was expecting 64 but got " + strconv.Itoa(n) + " bytes")
				f.Close()
			} else {
				// IMPLEMENTATION NOTE (rsn) - without locking the generator
				// we may overwrite it when other threads may be accessing it
				// through reseed calls.  when this happens (and likely in a
				// long running application it will), the output of this Fortuna
				// is NOT repeatable with the same startup params.  that is ok
				// since we only make guarantees about reproducibility for
				// Generator instances and not Fortuna's.
				//
				// RESEED(G, s)
				prng.generator.md.Write(s[0:64])
				prng.generator.reseed()

				f.Close()
				result = writeSeedFile(prng)
			}
		}
	}
	logTrace("<-- updateSeedFile()")
	return result
}

// updateSeedPeriodically saves the Fortuna random seed every 10 minutes.
func updateSeedPeriodically(f *Fortuna) {
	logInfo("updateSeedPeriodically(): Started...")
	for true {
		go updateSeedFile(f)
		time.Sleep(6e11) // 10 minutes
	}
}

// openSeedFile opens the Fortuna user's random seed file.
func openSeedFile(flag int) (*os.File, error) {
	return os.OpenFile(getSeedFilePath(), flag, 0600) // only u can r+w
}

// createSeedFile creates the file name and all parent sub-directories.
func createSeedFile() error {
	// NOTE (rsn) - the next commented out statements were for trying to use
	// $HOME/.go as the location for the random seed file.  we now use $GOROOT
	// which MUST be always there
	//	// ensure parent subdirectory(ies) are there
	//	e1 := os.MkdirAll(getSeedFileDirPath(), 0600) // only u can r+w
	//	if e1 != nil {
	//		return e1
	//	}
	f, e2 := os.OpenFile(getSeedFilePath(), os.O_WRONLY+os.O_CREATE, 0600) // only u can r+w
	if e2 != nil {
		return e2
	}
	return f.Close()
}

// getSeedFileDirPath returns the Fortuna random seed file parent folder.
// This directory is expected to be $GOROOT.
func getSeedFileDirPath() string {
	// NOTE (rsn) - was unable to store the random seed file in $USER's home
	// directory.  kept getting "permission denied"
	result := os.Getenv("GOROOT")
	logTrace("<-> getSeedFileDirPath(): " + result)
	return result
}

// getSeedFilePath returns the Fortuna random seed file path.
// This file is expected to be named '.random_seed' and located in $GOROOT.
func getSeedFilePath() string {
	// TODO (rsn) - check if there's a global func which returns the platform
	// specific file separator character
	result := getSeedFileDirPath() + "/.random_seed"
	logTrace("<-> getSeedFilePath(): " + result)
	return result
}
