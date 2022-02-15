from primegen import primeGen
import random
import math

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
    e = eGen(key.phi)
    
    return key
    


def privGen(phi,e):
    #TEMP
    d = pow(e, 1)
    return int(d)
