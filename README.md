# Encryption-Decryption-Algorithms
Implement some simple encryption and decryption algorithms

This repo implement some simple encryption/decryption algorithms, like RSA, ElGamal, Diffie-Hellman Key Exchange, ElGamal Re-Encryption, Universal ElGamal Re-Encryption. 

1. RSA Encryption/Decryption algorithm:

    (1) Key generation

    Generate a large primes p and q

    Compute n = p*q

    Compute phi = (p-1)(q-1)

    Generate a public key e by: gcd(e, phi), set (n, e) as public key

    Generate a private key d by: e.d ≡ 1 mod (n), set (n, d) as private key

    (2) Encryption:

    c = ciphertext

    m = plaintext

    c = m^e mod n

    (3) Decryption:

    m = c^d mod n

2. ElGamal Encryption/Decryption
    (1) Key generation:

    Given a large prime p = 65537, a primary root g = 3

    Choose a private key x between (1, p)

    Compute y = g^x mod p

    (2) Encryption:

    Choose a random number r between (1, p-1)

    Compute c1 = g^r mode p

    Compute c2 = m*(y^r mod p)

    (3) Decryption:

    m = c2/((c1)^r mod p)
