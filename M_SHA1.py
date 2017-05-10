import hashlib
import bitarray

class M_SHA1:
    def __init__(self):
        pass

    @staticmethod
    def performSHA1(inputString):
        m = hashlib.sha1()
        m.update(inputString)
        return m.hexdigest()