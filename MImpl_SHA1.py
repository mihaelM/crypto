import binascii


def rotl(num, bits):
    bit = num & (1 << (bits-1))
    num <<= 1
    if(bit):
        num |= 1
    num &= (2**bits-1)

    return num

def rotr(num, bits):
    num &= (2**bits-1)
    bit = num & 1
    num >>= 1
    if(bit):
        num |= (1 << (bits-1))

    return num

#cant use bytearray here eh
class MImpl_SHA1:

    #hexa zapis nam reducira duljinu 8 puta
    # 64 * 8 = 512
    # uzimljemo da je poruka isto u hexa zapisu ne
    @staticmethod
    def leftRotate(w, howMuch):
        lenW = len(w)

        rez = '0'*lenW
        for i in range(0, lenW):
            rez[i] = w[(i + howMuch) % lenW]

        return rez


    @staticmethod
    def xor4(w1, w2, w3, w4):

        rez = ''

        for a,b,c,d in w1, w2, w3, w4:
            k = (int(a) + int(b) + int(c) + int(d))%2
            rez += str(k)

        return rez

    @staticmethod
    def numToBinaryString(num):
        return "{0:b}".format(num)


    @staticmethod
    def hashMessage(message):

        h0 = 0x67452301
        h1 = 0xEFCDAB89
        h2 = 0x98BADCFE
        h3 = 0x10325476
        h4 = 0xC3D2E1F0

        message = ''.join(format(ord(x), 'b') for x in message)

        m1 = len(message)  # in bits I hope
        if m1 % 8 == 0:
            message += "10000000"

        while len(message) % 512 != 448:
            message += '0'

        m1BA = ''.join(format(ord(x), 'b') for x in str(m1))

        addition = '0' * (64 - m1)
        additionTotal = addition + m1BA

        message = additionTotal + message

        # sada idemo po chunkovima od 512 bita

        while len(message) > 0:

            tren = message[:512]
            message = message[512:]

            arr = []
            for i in range(0, 16):
                arr.append(tren[:32])
                tren = tren[32:]

            # extend 16 32 bit words into 80 32 bit words
            for i in xrange(16, 80):
                arr.append(MImpl_SHA1.leftRotate(MImpl_SHA1.xor4(arr[i - 3], arr[i - 8], arr[i - 14], arr[i - 16])))

            for i in xrange(0, 80):
                arr[i] = hex(int(arr[i], 2))

            a = h0
            b = h1
            c = h2
            d = h3
            e = h4

            for i in range(0, 80):

                f, k = None, None

                if i >= 0 and i <= 19:
                    f = (b & c) | ((~ b) & d)
                    k = 0x5A827999
                elif i >= 20 and i <= 39:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif i >= 40 and i <= 59:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif i >= 60 and i <= 79:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6

                # well see if rotl works or not on this hex strings

                temp = rotl(a, 5) + f + e + k + arr[i]
                e = d
                d = c
                c = rotl(b, 30)
                b = a
                a = temp

            h0 += a
            h1 += b
            h2 += c
            h3 += d
            h4 += e

        hh = (h0 << 128) | (h1 << 96) | (h2 << 64) | (h3 << 32) | h4

        return hh

