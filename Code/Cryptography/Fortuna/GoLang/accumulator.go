package fortuna

import (
	"io"
	"os"
	"sync"
	"time"
)

type entropySource interface {
	// Returns a unique ID in the range [0..255] identifying this source.
	getID() int

	// Returns the index of the Fortuna Pool to receive the next entropy bytes.
	getPoolNdx() int

	// Returns available entropy bytes and potential OS error.
	getEntropy() ([]byte, error)
}

var globalDevRandom = &devSource{id: 0, name: "/dev/random"}
var globalUserSeed = new(userSeed)
var globalDevURandom = &devSource{id: 2, name: "/dev/urandom"}

// TODO (rsn) - implement more collectors; e.g. a GPG seed reader

// Starts the known entropy collectors each in its own goroutine.
func startAccumulator() {
	go start(globalDevRandom)
	go start(globalUserSeed)
	go start(globalDevURandom)
}

func start(es entropySource) {
	logInfo("start(): Starting collector loop of entropy " + toString(es))
	for true {
		logDebug("start(): Getting entropy from " + toString(es))
		entropy, err := es.getEntropy() // will block until enough entropy is ready
		logDebug("Got entropy from " + toString(es))
		if err != nil {
			logWarn("start(): Unexpected error getting entropy from " + toString(es) + ": " + err.Error())
			// TODO (rsn) - investigate whether we should retry a few times
			// and if error persists, bail out altogether
		} else { // update Fortuna's pool at index poolNdx
			logDebug("start(): Updating Fortuna w/ entropy from " + toString(es))
			globalFortuna.updatePool(es.getPoolNdx(), es.getID(), entropy)
		}
	}
}

type devSource struct {
	lock    sync.Mutex
	id      int
	name    string
	f       *os.File
	poolNdx int
}

func (r *devSource) getID() int { return r.id }

func (r *devSource) getPoolNdx() int {
	result := r.poolNdx
	r.poolNdx = (r.poolNdx + 1) % 32
	return result
}

func (r *devSource) getEntropy() ([]byte, error) {
	logTrace("--> " + r.name + ".getEntropy()")
	r.lock.Lock()
	defer r.lock.Unlock()
	if r.f == nil {
		logInfo(r.name + ".getEntropy(): About to open device")
		f, err := os.OpenFile(r.name, os.O_RDONLY, 0)
		if f == nil {
			logError("Unable to open " + r.name + ": " + err.Error())
			return nil, err
		}
		r.f = f
	}
	buffer := make([]byte, 32) // maximum event size (p. 176)
	logDebug(r.name + ".getEntropy(): About to read 32 bytes")
	n, err := io.ReadFull(r.f, buffer)
	logTrace("<-- " + r.name + ".getEntropy()")
	return buffer[0:n], err
}

type userSeed struct {
	lock    sync.Mutex
	seed    int64
	ready   bool
	poolNdx int
}

func (r *userSeed) getID() int { return 1 }

func (r *userSeed) getPoolNdx() int {
	result := r.poolNdx
	r.poolNdx = (r.poolNdx + 1) % 32
	return result
}

func (r *userSeed) getEntropy() ([]byte, error) {
	logTrace("--> userSeed.getEntropy()")
	for true {
		r.lock.Lock()
		if r.ready {
			break
		}
		r.lock.Unlock()
		time.Sleep(1e9) // 1 second
	}
	result := toBytes(r.seed)
	r.ready = false
	r.lock.Unlock()
	logTrace("<-- userSeed.getEntropy()")
	return result, nil
}

func (r *userSeed) setSeed(seed int64) {
	r.lock.Lock()
	r.seed = seed
	r.ready = true
	r.lock.Unlock()
}

// Compile-time assertions
var _ entropySource = (*devSource)(nil)
var _ entropySource = (*userSeed)(nil)
