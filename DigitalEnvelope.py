
from M_RSA import *
from M_DES import *


class DigitalEnvelope:

    requires = ["Description:", "File name:", "Method:", "Key length:", "Envelope data:", "Envelope crypt key:"]
    def __init__(self):
        self.maps = {req : [] for req in DigitalEnvelope.requires}

    def loadRelevantData(self, fileName):
        readDataFromFile(fileName, self)

        # think about casting these variables !!!!
        self.description = self.maps["Description:"]
        self.fileName = self.maps["File name:"]
        self.method1 = self.maps["Method:"][0]
        self.method2 = self.maps["Method:"][1]
        self.keyLength1 = self.maps["Key length:"][0]
        self.keyLength2 = self.maps["Key length:"][1]
        self.envelopeData = mergeListToString(self.maps["Envelope data:"])
        self.envelopeCryptKey = mergeListToString(self.maps["Envelope crypt key:"])
        #^key for des

    def makeAnEnveleope(self, publicB):
#        self.envelopeData = addPadding(self.envelopeData)

        encryptionMess = M_DES.encryptWithDES(self.envelopeCryptKey, self.envelopeData)

       # print("Kriptiramo kljuc {}".format(self.envelopeCryptKey))
        encryptKey = M_RSA.encryptWithRSA(self.envelopeCryptKey, publicB)

       # print("Dobivamo {}".format(encryptKey))

        return (encryptionMess, encryptKey)

    @staticmethod
    def openAnEnvelope(encryptionMess, encryptKey, privateB):

        decrypKey = M_RSA.decryptWithRSA(encryptKey, privateB)

        decrypMess = M_DES.decryptWithDES(decrypKey, encryptionMess)

        return decrypMess