import rsa
import random
import math
from random import randint
def generate_prime(start, end): 
    l = list() 
    for i in range(start, end+1): 
        flag = True
        for j in range(2, i): 
            if i % j == 0: 
                flag = False
                break
        if flag: 
            l.append(i) 
    size = len(l)
    # print(size)
    i = randint(0, size-1)
    return l[i]

def gcd(a, b):
    while b!= 0:
        a, b = b, a % b
    return a


def generate_e(p, q):
    phia = (p-1)*(q-1)
    e = random.randrange(1, phia)
    g = gcd(e, phia)
    while g != 1:
        e = random.randrange(1, phia)
        g = gcd(e, phia)
    # print(e)
    return e

def modInverse(a, m) : 
    a = a % m
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

def generate_d(e, pq):
    d = modInverse(e, pq)
    # print(d) 
    return d

def encryption(m, n, e):
    temp = m ** e
    cipher = temp % n
    # print('ciphertext is ' + str(cipher))
    return cipher

def decryption(c, n, d):
    temp = c ** d
    plaintext = temp % n
    # print('plaintext is ' + str(plaintext))
    return plaintext
def main():
    # generate p and q
    print('           RSA Encryption/Decryption          ')
    p = generate_prime(1000, 1050)
    q = generate_prime(1000, 2000)
    print('**********************************************')
    print('1. Generate primes p and q (1000< p, q < 5000)')
    print('p = ' + str(p))
    print('q = ' + str(q))

    # calculate p*q
    print('**********************************************')
    print('2. Compute n = pq')
    n = p*q
    print('n = ' + str(n))
    
    # set a public key
    print('**********************************************')
    e = generate_e(p, q)
    phia = (p-1)*(q-1)
    print('3. Set a public key e')
    print('e = ' + str(e))

    # private key d
    print('**********************************************')
    d = generate_d(e, phia)
    print('4. Calculate the private key d')
    print('d = ' +str(d))

    # input of a plaintext
    print('**********************************************')
    message = input('5. Input a message m in the keyboard: ')
    print('m = ' + str(message))
    message = int(message)

    # encryption
    c = encryption(message, n, e)
    print('**********************************************')
    print('6. Encrypt c = m^e modn, c = ' + str(c))

    # decryption    
    plaintext = decryption(c, n, d)
    print('**********************************************')
    print('7. Decrypt m = c^d mod n, m = ' + str(plaintext))
    print('**********************************************')
if __name__ == "__main__":
    main()