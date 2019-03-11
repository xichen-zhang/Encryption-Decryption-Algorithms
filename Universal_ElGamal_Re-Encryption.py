import random


def main():
    print('            Universal ElGamal Re-encryption            ')
    print('*******************************************************')
    print('0. Given a large prime p = 65537, a primary root g = 3')
    print('*******************************************************')
    p = 65537
    g = 3
    a = random.randint(1, p)
    print('1. Choose a private key a in the range of [1, p-1], a = ' + str(a))
    print('*******************************************************')
    print('2. Compute the corresponding public key A = g^a mod p')
    A = g ** a
    A = A % p
    print('     A = ' + str(A))
    print('*******************************************************')
    m = input('3. Input a message m in the keyboard: m = ')
    m = int(m)
    print('*******************************************************')
    print('4. Encryption')
    r = random.randint(1, p-1)
    print('     4.1 Choose a random unmber r, r = ' + str(r))
    s = random.randint(1, p-1)
    print('     4.2 Choose a random unmber r, s = ' + str(s))
    X = A ** r
    X = X % p
    X = X * m
    print('     4.3 X = m * A^r mod p, X = ' + str(X))
    Y = g ** r
    Y = Y % p
    print('     4.4 Y = g^r mod p, Y = ' + str(Y))
    W = A ** s
    W = W % p
    print('     4.5 W = A^s mod p, W = ' + str(W))
    Z = g ** s
    Z = Z % p
    print('     4.6 Z = g^s mod p, Z = ' + str(Z))
    print('*******************************************************')
    print('5. Re-Encryption')
    r1 = random.randint(1, 100)
    print('     5.1 Choose a random unmber r1, r1 = ' + str(r1))
    r2 = random.randint(1, 100)
    print('     5.2 Choose a random unmber r2, r2 = ' + str(r2))
    temp = r + s*r1
    X1 = A ** temp
    X1 = X1 % p
    X1 = X1 * m
    print('     5.3 X1 = m * A^(r + s*r1) % p, X1 = ' + str(X1))
    Y1 = Z ** r1
    Y1 = Y1 % p
    Y1 = Y * Y1
    print('     5.4 Y1 = Y * Z^r1 % p, Y1 = ' + str(Y1))
    W1 = W ** r2
    W1 = W1 % p
    print('     5.5 W1 = W^r2 % p, W1 = ' +str(W1))
    Z1 = Z**r2
    Z1 = Z1 % p
    print('     5.6 Z1 = Z^r2 % p, Z1 = ' + str(Z1))
    print('*******************************************************')
    print(' 6. Decryption')
    temp = Y1 ** a
    temp = temp % p
    results = X1 / temp
    print('     6.1 the plaintext m = X1 / (Y1)^a: m = ' + str(results))
    temp1 = Z1 ** a
    temp1 = temp1 % p
    results1 = W1 / temp1
    print('     6.2 check if identifier = W1 / (Z^a) = 1 mod p, identifier = ' + str(results1))
    if(results1 == 1):
        print('Accepted!')
    else:
        print('Rejected!')





    # c1 = g ** r
    # c1 = c1 % p
    # print('     4.2 Compute c1 = g^r mod p, c1 = ' + str(c1))
    # c2 = y ** r
    # c2 = c2 % p
    # c2 = m * c2
    # print('     4.3 Compute c2 = m*y^r mod p, c2 = ' + str(c2))
    # print('*******************************************************')
    # print('5. Decryption C = (c1, c2)')
    # temp = c1 ** x
    # temp = temp % p
    # result =  c2/temp
    # print('     m= c2/c1^x mod p, m = ' + str(result))

if __name__ == "__main__":
    main()