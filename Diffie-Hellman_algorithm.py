import random

def main():
    print('            Diffie-Hellman Key Exchange              ')
    print('*****************************************************')
    print('0. Given a large prime p = 65537, a primary root g = 3')
    p = 65537
    g = 3
    print('*****************************************************')
    print('1. Choose a random number x')
    x = random.randint(1, p-1)
    print('     x = ' + str(x))
    print('*****************************************************')
    print('2. Compute X = g^x mod p')
    X = g**x
    X = X % p
    print('     X = ' + str(X))
    print('*****************************************************')
    print('3. Choose a random number y')
    y = random.randint(1, p-1)
    print('     y = ' + str(y))
    print('*****************************************************')
    print('4. Compute Y = g^y mod p')
    Y = g**y
    Y = Y % p
    print('     Y = ' + str(Y))
    print('*****************************************************')
    print('5. Calculate the session key K = g ^ xy mod p')
    K1 = Y ** x
    K1 = K1 % p
    K2 = X ** y
    K2 = K2 % p
    print('K = Y^x mod p = ' + str(K1) + '     K = X^y mod p' + str(K2))

if __name__ == "__main__":
    main()