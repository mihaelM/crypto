from helperFuns import *
#from Crypto.Cipher import DES
import os
from pyDes import *

class M_DES:
    requires = ["Description:", "File name:", "Data:"]
    def __init__(self):
        self.maps = {req : [] for req in M_DES.requires}


    def loadRelevantData(self, fileName):
        readDataFromFile(fileName, self)

        # think about casting these variables !!!!
        self.description = self.maps["Description:"]
        self.fileName = self.maps["File name:"]
        self.data = mergeListToString(self.maps["Data:"])
       # self.key = M_DES.generateDESKey()

    @staticmethod
    def encryptWithDES(key, data):
        k = des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        return k.encrypt(data)

    @staticmethod
    def decryptWithDES(key, cipher_text):
        k = des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        return k.decrypt(cipher_text)


    @staticmethod
    def generateDESKey():
        return os.urandom(4).encode('hex')