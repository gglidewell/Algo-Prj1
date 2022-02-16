def SigEncrypt(sig, d, n):
     for x in sig:
        x = pow(ord(x),d,n)
        auth.append(x)

def SigDecrypt(e, n):
    name = ""
    for x in auth:
        x = pow(x,e,n)
        name += chr(x)
    return(name)
