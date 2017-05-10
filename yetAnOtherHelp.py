import binascii
from Crypto.PublicKey import RSA
from M_SHA1 import *

def bin2hex(binStr):
    return binascii.hexlify(binStr)


def hex2bin(hexStr):
    return binascii.unhexlify(hexStr)


key = RSA.generate(2048)

binPrivKey = key.exportKey()
print(binPrivKey)

binPubKey =  key.publickey().exportKey()
print(binPubKey)


privKeyObj = RSA.importKey(binPrivKey)
pubKeyObj =  RSA.importKey(binPubKey)

msg = "attack at dawn"
emsg = pubKeyObj.encrypt(msg, 'x')
dmsg = privKeyObj.decrypt(emsg)


print (dmsg)

assert(msg == dmsg)