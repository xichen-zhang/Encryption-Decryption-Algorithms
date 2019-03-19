import random
import sys
import math
import primes

def ipow(a, b, n):
    """calculates (a**b) % n via binary exponentiation, yielding itermediate
       results as Rabin-Miller requires"""
    A = a = long(a % n)
    yield A
    t = 1
    while t <= b:
        t <<= 1

    # t = 2**k, and t > b
    t >>= 2
    
    while t:
        A = (A * A) % n
        if t & b:
            A = (A * a) % n
        yield A
        t >>= 1

def rabin_miller_witness(test, possible):
    """Using Rabin-Miller witness test, will return True if possible is
       definitely not prime (composite), False if it may be prime."""    
    return 1 not in ipow(test, possible-1, possible)

smallprimes = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,
               47,53,59,61,67,71,73,79,83,89,97)

def default_k(bits):
    return max(40, 2 * bits)

def is_probably_prime(possible, k=None):
    if possible == 1:
        return True
    if k is None:
        k = default_k(possible.bit_length())
    for i in smallprimes:
        if possible == i:
            return True
        if possible % i == 0:
            return False
    for i in xrange(k):
        test = random.randrange(2, possible - 1) | 1
        if rabin_miller_witness(test, possible):
            return False
    return True

def generate_prime(bits, k=None):
    """Will generate an integer of b bits that is probably prime 
       (after k trials). Reasonably fast on current hardware for 
       values of up to around 512 bits."""    
    assert bits >= 8

    if k is None:
        k = default_k(bits)

    while True:
        possible = random.randrange(2 ** (bits-1) + 1, 2 ** bits) | 1
        if is_probably_prime(possible, k):
            return possible

def invmod(a, p, maxiter=1000000):
    """The multiplicitive inverse of a in the integers modulo p:
         a * b == 1 mod p
       Returns b.
       (http://code.activestate.com/recipes/576737-inverse-modulo-p/)"""
    if a == 0:
        raise ValueError('0 has no inverse mod %d' % p)
    r = a
    d = 1
    for i in range(min(p, maxiter)):
        d = ((p // r + 1) * d) % p
        r = (d * a) % p
        if r == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (a, p))
    return d

def modpow(base, exponent, modulus):
    """Modular exponent:
         c = b ^ e mod m
       Returns c.
       (http://www.programmish.com/?p=34)"""
    result = 1
    while exponent > 0:
        if exponent & 1 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

class PrivateKey(object):

    def __init__(self, p, q, n):
        self.l = (p-1) * (q-1)
        self.m = invmod(self.l, n)

    def __repr__(self):
        return '<PrivateKey: %s %s>' % (self.l, self.m)

class PublicKey(object):

    @classmethod
    def from_n(cls, n):
        return cls(n)

    def __init__(self, n):
        self.n = n
        self.n_sq = n * n
        self.g = n + 1

    def __repr__(self):
        return '<PublicKey: %s>' % self.n

def generate_keypair(bits):
    p = primes.generate_prime(bits / 2)
    q = primes.generate_prime(bits / 2)
    n = p * q
    # print(p)
    # print(q)
    return PrivateKey(p, q, n), PublicKey(n)

def encrypt(pub, plain):
    while True:
        r = primes.generate_prime(int(round(math.log(pub.n, 2))))
        if r > 0 and r < pub.n:
            break
    x = pow(r, pub.n, pub.n_sq)
    cipher = (pow(pub.g, plain, pub.n_sq) * x) % pub.n_sq
    return cipher

def e_add(pub, a, b):
    """Add one encrypted integer to another"""
    return a * b % pub.n_sq

def e_add_const(pub, a, n):
    """Add constant n to an encrypted integer"""
    return a * modpow(pub.g, n, pub.n_sq) % pub.n_sq

def e_mul_const(pub, a, n):
    """Multiplies an ancrypted integer by a constant"""
    return modpow(a, n, pub.n_sq)

def decrypt(priv, pub, cipher):
    x = pow(cipher, priv.l, pub.n_sq) - 1
    plain = ((x // pub.n) * priv.m) % pub.n
    return plain

def Paillier_Homo():
    print('               Paillier Homomorphic Encryption Algorithm                    ')
    print('\n')
    print('**********************************************************************************************************')
    print(' 1. Generate public keys and private keys:')
    private_key, public_key = generate_keypair(128)
    g = public_key.g
    n = public_key.n
    n_squre = public_key.n_sq
    print(' ============ Print Public Key ============')
    print(' Public key: g = ' + str(g))
    print(' Public key: n = ' +str(n))
    print(' Public key: n_squre = ' + str(n_squre))
    print(' ============ Print Private Key ============')
    l = private_key.l
    u = private_key.m
    print(' Private key: l = ' + str(l))
    print(' Private key: u = ' +str(u))
    print('\n')
    print(' 2. Type the inputs for testing the algorithm:')
    print('**********************************************************************************************************')
    m1 = input(' Input the first message m1 in the keyboard: m1 = ')
    m1 = int(m1)
    m2 = input(' Input the second message m2 in the keyboard: m2 = ')
    m2 = int(m2)
    print('\n')
    print(' 3. Encryption:')
    print('**********************************************************************************************************')
    c1 = encrypt(public_key, m1)
    c2 = encrypt(public_key, m2)
    print(' Ciphertext for m1 is c1, c1 = ' + str(c1))
    print(' Ciphertext for m2 is c2, c2 = ' + str(c2))
    print('\n')
    print(' 4. Decryption:')
    print('**********************************************************************************************************')
    de_m1 = decrypt(private_key, public_key, c1)
    de_m2 = decrypt(private_key, public_key, c2)
    print(' After decryption, the plaintext of c1 is : ' + str(de_m1))
    print(' After decryption, the plaintext of c2 is : ' + str(de_m2))
    print('\n')
    print(' 5. Homomorphic Testing:')
    print('**********************************************************************************************************')
    temp = c1 * c2 % public_key.n_sq
    print(' c1 multiple by c2 mod n_square is :' + str(temp))
    m1_plus_m2 = decrypt(private_key, public_key, temp)
    print(' after decryption, m1 + m2 is ' + str(m1_plus_m2))
    print(' Test Done!')
def main():
    Paillier_Homo()

if __name__ == "__main__":
    main()