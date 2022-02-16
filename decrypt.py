def decrypt(c, d, n):
    
    de = pow(c, d, n)
    print("decrypted data: ", de)
    
    return de