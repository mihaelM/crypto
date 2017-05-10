def readDataFromFile(fileName, relevantClass): # name of algorithm class
    file = open(fileName, "r")
    lines = file.readlines()
    begin = False
    state = None #what do we currently load

    for line in lines:

        if begin:
            if (len(line.strip()) == 0):
                continue

            if state:
                #if starts with empty, sth and continue
                if line.startswith("    "):
                    stripLine = line.strip()
                    relevantClass.maps[state].append(stripLine)

            for option in relevantClass.requires:
                if line.startswith(option):
                    state = option
                    break

        if (line.startswith("---BEGIN OS2 CRYPTO DATA---")):
            begin = True

        if (line.startswith("---END OS2 CRYPTO DATA---")):
            break



def mergeListToString (lis):
    return ''.join(lis)


def mergeListToString2(lis):
    return '\n'.join(lis)


"""
def switchFromPrivateToPublic(key):

    key = key.replace("-----BEGIN RSA PRIVATE KEY-----", "-----BEGIN PUBLIC KEY-----")
    key = key.replace("-----END RSA PRIVATE KEY-----", "-----END PUBLIC KEY-----")
    return key

def switchFromPublicToPrivate(key):

    key = key.replace("-----BEGIN PUBLIC KEY-----", "-----BEGIN RSA PRIVATE KEY-----")
    key = key.replace("-----END PUBLIC KEY-----", "-----END RSA PRIVATE KEY-----")
    return key

"""
