from helperFuns import *
from M_SHA1 import *
from M_RSA import *

class DigitalSignature:
    requires = ["Description:", "File name:", "Method:", "Key length:", "Signature data:"]
    def __init__(self):
        self.maps = {req : [] for req in DigitalSignature.requires}

    def loadRelevantData(self, fileName):
        readDataFromFile(fileName, self)

        # think about casting these variables !!!!
        self.description = self.maps["Description:"]
        self.fileName = self.maps["File name:"]
        self.method1 = self.maps["Method:"][0]
        self.method2 = self.maps["Method:"][1]
        self.keyLength1 = self.maps["Key length:"][0]
        self.keyLength2 = self.maps["Key length:"][1]
        self.signatureData = mergeListToString(self.maps["Signature data:"])

    #for now we imported message via function
    def makeASignature(self, privateA):

        # we have to map this key so it says it is public (though it is not)

        hashedMessage = M_SHA1.performSHA1(self.signatureData)

        encryptedHash = M_RSA.decryptWithRSA(hashedMessage, privateA)

        print("poruka je\n{}".format(self.signatureData))
        print ("hashirano je\n{}".format(hashedMessage))

        return (self.signatureData, encryptedHash)

    @staticmethod
    def checkSignature(message, cryptedHash, publicA):
        #get message
        #decrypt signature with publicA
        #caclulate hash and compare

        hashedMessage = M_SHA1.performSHA1(message)
        print("hashirana poruka je {}".format(hashedMessage))

        decryptedHash = M_RSA.encryptWithRSA(cryptedHash, publicA)
        print ("dekrptirani hash je {}".format(decryptedHash[0]))


        return hashedMessage == decryptedHash[0]

