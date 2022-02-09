def primeGen():
    # referenced from https://www.delftstack.com/howto/python/python-generate-prime-number/#:~:text=Under%20the%20Python%20random%20module,choice()%20.
    primes = []
    for n in range(0, 99):
        prime = True
        
        for num in range(2, n):
            if n % num == 0:
                prime = False
                
        if prime:
            primes.append(n)
            
    return primes    
            
