from primegen import primeGen
import random
import math

#REF FROM https://stackoverflow.com/questions/55554166/how-to-calculate-rsa-private-key-in-python/55554571

class publicKey:
    n = 0
    e = 0
    phi = 0

def eGen(phi):
    e = 3

    while e <= phi:
        a = phi
        b = e

        while b:
            a, b = b, a % b

        if a == 1:
            return e
        else:
            e += 2


def pubGen():
    key = publicKey()
    
    p = primeGen()
    q = primeGen()
    key.n = p*q
    key.phi = (p-1)*(q-1)
    key.e = eGen(key.phi)
    
    return key
    


def euclid(a, b):

    if a == 0:
        return b, 0, 1
    else:
        g, y, x = euclid(b % a, a)
        return g, x - (b // a) * y, y


def privGen(e, phi):
    g, x, y = euclid(e, phi)

    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi