import random


def main():
    print('              ElGamal Encryption/Decryption            ')
    print('*******************************************************')
    print('0. Given a large prime p = 65537, a primary root g = 3')
    print('*******************************************************')
    p = 65537
    g = 3
    x = random.randint(1, p)
    print('1. Choose a private key x, x = ' + str(x))
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
    print('     4.1 Choose a random unmber r, r = ' + str(r))
    c1 = g ** r
    c1 = c1 % p
    print('     4.2 Compute c1 = g^r mod p, c1 = ' + str(c1))
    c2 = y ** r
    c2 = c2 % p
    c2 = m * c2
    print('     4.3 Compute c2 = m*y^r mod p, c2 = ' + str(c2))
    print('*******************************************************')
    print('5. Decryption C = (c1, c2)')
    temp = c1 ** x
    temp = temp % p
    result =  c2/temp
    print('     m= c2/c1^r mod p, m = ' + str(result))

if __name__ == "__main__":
    main()