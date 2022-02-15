from primegen import primeGen
import random
import math

class publicKey:
    n = 0
    e = 0
    phi = 0

def pubGen():
    key = publicKey()
    
    p = primeGen()
    q = primeGen()
    key.n = p*q
    key.phi = (p-1)*(q-1)
    
    #E GEN
    for i in range(key.phi):
        if(math.gcd(i, key.phi) == 1 and i > 1):
            key.e = i
            break
    return key
    

def privGen(phi,e):
    d = pow(e, -1)
    return int(d)
