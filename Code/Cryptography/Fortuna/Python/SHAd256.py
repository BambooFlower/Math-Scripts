"""\
SHA_d-256 hash function implementation.
This module should comply with PEP 247.
"""

__revision__ = "$Id$"
__all__ = ['new', 'digest_size']

import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    from Crypto.Util.py21compat import *
from Crypto.Util.py3compat import *

from binascii import b2a_hex

from Crypto.Hash import SHA256

assert SHA256.digest_size == 32

class _SHAd256(object):
    """SHA-256, doubled.
    Returns SHA-256(SHA-256(data)).
    """

    digest_size = SHA256.digest_size

    _internal = object()

    def __init__(self, internal_api_check, sha256_hash_obj):
        if internal_api_check is not self._internal:
            raise AssertionError("Do not instantiate this class directly.  Use %s.new()" % (__name__,))
        self._h = sha256_hash_obj

    # PEP 247 "copy" method
    def copy(self):
        """Return a copy of this hashing object"""
        return _SHAd256(SHAd256._internal, self._h.copy())

    # PEP 247 "digest" method
    def digest(self):
        """Return the hash value of this object as a binary string"""
        retval = SHA256.new(self._h.digest()).digest()
        assert len(retval) == 32
        return retval

    # PEP 247 "hexdigest" method
    def hexdigest(self):
        """Return the hash value of this object as a (lowercase) hexadecimal string"""
        retval = b2a_hex(self.digest())
        assert len(retval) == 64
        if sys.version_info[0] == 2:
            return retval
        else:
            return retval.decode()

    # PEP 247 "update" method
    def update(self, data):
        self._h.update(data)

# PEP 247 module-level "digest_size" variable
digest_size = _SHAd256.digest_size

# PEP 247 module-level "new" function
def new(data=None):
    """Return a new SHAd256 hashing object"""
    if not data:
        data=b("")
    sha = _SHAd256(_SHAd256._internal, SHA256.new(data))
    sha.new = globals()['new']
    return sha
