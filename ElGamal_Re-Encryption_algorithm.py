import random


def main():
    print('            ElGamal Re-Encryption Algorithm            ')
    print('*******************************************************')
    print('0. Given a large prime p = 65537, a primary root g = 3')
    print('*******************************************************')
    p = 65537
    g = 3
    x = random.randint(1, p)
    print('1. Choose a private key x in the range of [1, p-1], x = ' + str(x))
    print('*******************************************************')
    print('2. Compute the corresponding public key y = g^x mod p')
    y = g ** x
    y = y % p
    print('     y = ' + str(y))
    print('*******************************************************')
    m = input('3. Input a message m in the keyboard: m = ')
    m = int(m)
    print('*******************************************************')
    print('4. Encryption')
    r = random.randint(1, p-1)
    print('     4.1 Choose a random unmber r in range of [1, p-1], r = ' + str(r))
    c1 = g ** r
    c1 = c1 % p
    print('     4.2 Compute c1 = g^r mod p, c1 = ' + str(c1))
    c2 = y ** r
    c2 = c2 % p
    c2 = m * c2
    print('     4.3 Compute c2 = m*y^r mod p, c2 = ' + str(c2))
    print('*******************************************************')
    print('5. Re-encryption')
    print('*******************************************************')
    r1 = random.randint(1, p-1)
    print('     5.1 Choose a random number r1 in range of [1, p-1], r1 = ' + str(r1))
    r3 = r + r1
    c3 = g ** r3
    c3 = c3 % p
    print('     5.2 Compute c3 = c1 * g^r1 mode p, c3 = ' + str(c3))
    c4 = y ** r3
    c4 = c4 % p
    c4 = m * c4
    print('     5.3 Compute c4 = c2 * y^r1 mode p, c4 = ' + str(c4))
    print('*******************************************************')
    print('6. Decryption C = (c3, c4)')
    temp = c3 ** x
    temp = temp % p
    result =  c4/temp
    print('     m= c4/c3^x mod p, m = ' + str(result))

if __name__ == "__main__":
    main()