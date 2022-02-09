from primegen import primeGen
import random

class publicKey:
    n = 0
    e = 0
    phi = 0


def eGen(n, phi):
    valid = False
    
    #check not a factor of n
    while not valid:
        num = random.randint(2, phi)
        if n % num != 0:
            valid = True
    return num

def pubGen():
    key = publicKey()
    
    p = primeGen()
    q = primeGen()
    key.n = p*q
    key.phi = (p-1)*(q-1)
    key.e = eGen(key.n, key.phi)
    return key
    

def privGen(phi,e):
    k = random.randint(2, 100)
    d = (k*phi + 1)/e
    
    return int(d)
