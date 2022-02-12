import math
def encrypt(message, e, n):
    toEncrypt = ""
    
    # ref from https://www.delftstack.com/howto/python/convert-letter-to-number-python
    for x in message:
        toEncrypt += str(ord(x) - 96)
    #encrypt: c = (msg^e) %n
    print("Message in numbers: ", toEncrypt)
    c = pow(int(toEncrypt), e, n)
    print("c: ", c)
    
    return c
    