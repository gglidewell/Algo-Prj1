import math
#Signature Generation
def sEncrypt(c, d, n):
    S = pow(c,d) % n
    return S

#Signature Verification
def sDecrypt(S, e, n):
    I = pow(S,e) % n
    return I