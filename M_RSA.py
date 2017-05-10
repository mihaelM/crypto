from helperFuns import *
from Crypto.PublicKey import RSA

class M_RSA_private:
    requires = ["Description:", "Method:", "Key:"]

    def __init__(self):
        self.maps = {req : [] for req in M_RSA_private.requires}

    def loadRelevantData(self, fileName):
        readDataFromFile(fileName, self)
        self.description = self.maps["Description:"]
        self.method = self.maps["Method:"]
        self.key = mergeListToString2(self.maps["Key:"])



class M_RSA_public:
    requires = ["Description:", "Method:", "Key:"]

    def __init__(self):
        self.maps = {req : [] for req in M_RSA_private.requires}

    def loadRelevantData(self, fileName):
        readDataFromFile(fileName, self)

        self.description = self.maps["Description:"]
        self.method = self.maps["Method:"]
        self.key = mergeListToString2(self.maps["Key:"])


# sad bi RSA trebao radit iako nije testirano
class M_RSA:


    @staticmethod
    def encryptWithRSA(message, mRSApublic):
      #  print(mRSApublic.key) # bi trebo bit bas onaj kljuc ne

        pubKeyObj = RSA.importKey(mRSApublic.key)
        return pubKeyObj.encrypt(message, 'x') # x does not have purpose

    @staticmethod
    def decryptWithRSA(cypherText, mRSAprivate):
      #  print(mRSAprivate.key)
        privKeyObj = RSA.importKey(mRSAprivate.key)

        return privKeyObj.decrypt(cypherText)

