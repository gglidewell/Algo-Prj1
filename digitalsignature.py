#Signature Generation
def sEncrypt(c, d, n):
    s = pow(int(c),d,n)
    return s

#Signature Verification
def sDecrypt(s, e, n):
    i = pow(s,e,n)
    return i