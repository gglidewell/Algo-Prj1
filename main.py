from primegen import primeGen
from keygen import eGen
from keygen import privGen
import random
userType = 0
publicChoice = 0
privateChoice = 0
messageChoice = 0
publicMessage = ""
privateMessage = ""
signature = ""
p = 0;
q = 0;
n = 0;
phi = 0
privKey = 0
#TODO: SIMPLIFY PUBLIC KEYGEN TO KEYGEN.PY, MAYBE STRUCT? -h

p = random.choice(primeGen())
q = random.choice(primeGen())
n = p*q
phi = (p-1)*(q-1)
e = eGen(n, phi)
privKey = privGen(phi, e)

#TODO: REMOVE LATER
print("p:", p)
print("q:", q)
print("n:", n)
print("phi:", phi)
print("e:", e)
print("privkey: ", privKey)

while True:
    print("RSA Keys has been generated")
    print("Please select your user type")
    print("\n1. A public user")
    print("\n2. The owner of the key")
    print("\n3. Exit program")
    userType = int(input("Enter your choice: "))
    
    while userType == 1:
        print("As a public user, what would you like to do?")
        print("\n1. Send an encrypted message")
        print("\n2. Authenticate a digital signature")
        print("\n3. Exit")
        publicChoice = int(input("Enter your choice: "))
        
        if publicChoice == 1:
            publicMessage = int(input("Enter a message: "))
            print("Message encrypted and sent")
            #CODE HERE
            
        if publicChoice == 2:
            if signature is None:
                print("There are no signature to authenticate")
            else:
                print("The following messages are available: ")
                print("\n1. ", signature)
                #CODE HERE
        
        if publicChoice == 3:
            userType = 0
                
    while userType == 2:
        print("As the owner of the keys, what would you like to do?")
        print("\n1. Decrypt a received message")
        print("\n2. Digitally sign a message")
        print("\n3. Exit")
        privateChoice = int(input("Enter your choice: "))
        
        if privateChoice == 1:
            if privateMessage is None:
                print("There are no messages available")
            else:
                print("The following messages are available: ")
                print("\n1. (length = ", len(privateMessage), ")")
                messageChoice = input("Enter your choice: ")
                
                if messageChoice == 1:
                    print("Decrypted message: ")
                    #CODE HERE
                
        if privateChoice == 2:
            privateMessage = input("Enter a message: ")
            #CODE HERE
            print("Message signed and sent")
            
        if privateChoice == 3:
            userType = 0
                
    if userType == 3:
        break