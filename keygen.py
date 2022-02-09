import random
def eGen(n, phi):
    valid = False
    
    #check not a factor of n
    while not valid:
        num = random.randint(2, phi)
        if n % num != 0:
            valid = True
    return num

def privGen(phi,e):
    k = random.randint(2, 100)
    d = (k*phi + 1)/e
    
    return int(d)
