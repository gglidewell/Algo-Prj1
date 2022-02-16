#Signature Generation
def sEncrypt(c, d, n):
S = (c**d) % n
return S

#Signature Verification
def sDecrypt(S, e, n):
I = (S**e) % n
return I