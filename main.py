import pickle
from DigitalEnvelope import *
from DigitalSignature import *

def printMessage():
    print("")
    print("Sve od sljedecih 6 operacija ce se generirati nad defaultnim, ali promjenjivim dokumentima.")
    print("Pritisnite 1 za generiranje digitalne omotnice.")
    print("Pritisnite 2 za otvaranje digitalne omotnice.")
    print("Pritisnite 3 za generiranje defaultnog digitalnog potpisa.")
    print("Pritisnite 4 za provjeru digitalnog potpisa")
    print("Pritisnite 5 za generiranje digitalnog pecata")
    print("Pritisnite 6 za provjeru digitalnog pecata")
    print("")

def generateMessage():


    while True:

        printMessage()
        line = raw_input()
        line = line.strip()

        if line == "1":
            generateEnveleope()
        elif line == "2":
            openEnveleope()
        elif line == "3":
            generateDigitalSignature()
        elif line == "4":
            checkDigitalSignature()
        elif line == "5":
            generateDigitalStamp()
        elif line == "6":
            checkDigitalStamp()
        elif line == "X":
            return



def generateEnveleope():

    # we do not use ulazni_tekst.txt -> redundant
    # also des info is read

    digitalEnveleope = DigitalEnvelope()
    digitalEnveleope.loadRelevantData("digital_envelope.txt")

    publicB = M_RSA_public()
    publicB.loadRelevantData("RSA_public_key_B.txt")

    encryptionMess, encryptKey = digitalEnveleope.makeAnEnveleope(publicB)

    #write these to pickle, serialization
    file = open('generatedEnvelpe.pickle', 'w+')
    pickle.dump([encryptionMess, encryptKey], file)

    print("Omotnica je uspjesno generirana")

   # print(encryptionMess)
   # print("KKKK")
   # print(encryptKey)

def openEnveleope(): #error if does not exist

    try:
        file = open('generatedEnvelpe.pickle')
    except:
        print("Omotnica ne postoji\n")
        return

    encryptionMess, encryptKey = pickle.load(file)

    privateB = M_RSA_private()
    privateB.loadRelevantData("RSA_private_key_B.txt")
    decryptMessage = DigitalEnvelope.openAnEnvelope(encryptionMess, encryptKey, privateB)

    print ("Omotnica je uspjesno otvorena.")
    print ("Dekriptirana poruka je:")
    print(decryptMessage)

    return

def generateDigitalSignature():
    digitalSignature = DigitalSignature()
    digitalSignature.loadRelevantData("digital_signature.txt")
    # treba vidjet kaj s ovim messagom svakako

    privateA = M_RSA_private()
    privateA.loadRelevantData("RSA_private_key_A.txt")

    message, encryptedHash = digitalSignature.makeASignature(privateA)


    file = open('generatedSignature.pickle', 'w+')
    pickle.dump([message, encryptedHash], file)

    print("Poruka je uspjesno digitalno potpisana.")


def checkDigitalSignature():

    try:
        file = open('generatedSignature.pickle')
    except:
        print("Potpis ne postoji\n")
        return

    message, encryptedHash = pickle.load(file)

    publicA = M_RSA_public()
    publicA.loadRelevantData("RSA_public_key_A.txt")

    isSigned = DigitalSignature.checkSignature(message, encryptedHash, publicA)

    if isSigned:
        print("Potpisano je.")
        print("Osigurana je autoneticnost, integritet i neporecivost!\n")
    else:
        print("Nije potpisano.")
        print("Nije osigurana je autoneticnost, integritet i neporecivost!\n")





def generateDigitalStamp():

    #digitalno potpisana digitalna omotnica u smislu da se ne salje poruka direktno nego kriptira

#envelope
    digitalEnveleope = DigitalEnvelope()
    digitalEnveleope.loadRelevantData("digital_envelope.txt")

    publicB = M_RSA_public()
    publicB.loadRelevantData("RSA_public_key_B.txt")

    encryptionMess, encryptKey = digitalEnveleope.makeAnEnveleope(publicB)

#signature
    digitalSignature = DigitalSignature()
    digitalSignature.loadRelevantData("digital_signature.txt")
    # treba vidjet kaj s ovim messagom svakako

    privateA = M_RSA_private()
    privateA.loadRelevantData("RSA_private_key_A.txt")

    message, encryptedHash = digitalSignature.makeASignature(privateA)

    file = open('generatedDigitalStamp.pickle', 'w+')
    pickle.dump([encryptionMess, encryptKey, encryptedHash], file)

    return




def checkDigitalStamp():
    try:
        file = open('generatedDigitalStamp.pickle')
    except:
        print("Potpis ne postoji\n")
        return

    encryptionMess, encryptKey, encryptedHash = pickle.load(file)


    privateB = M_RSA_private()
    privateB.loadRelevantData("RSA_private_key_B.txt")
    decryptMessage = DigitalEnvelope.openAnEnvelope(encryptionMess, encryptKey, privateB)

    publicA = M_RSA_public()
    publicA.loadRelevantData("RSA_public_key_A.txt")

    isSigned = DigitalSignature.checkSignature(decryptMessage, encryptedHash, publicA)


    if isSigned:
        print("Potpisano je.")
        print("Osigurana je tajnost, autoneticnost, integritet i neporecivost!\n")
    else:
        print("Nije potpisano.")
        print("Nije osigurana je tajnost, autoneticnost, integritet i neporecivost!\n")



if __name__ == "__main__":
    generateMessage()









