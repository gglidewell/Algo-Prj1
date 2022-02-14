from keygen import privGen
from keygen import pubGen
from encrypt import encrypt
from decrypt import decrypt

userType = 0
publicChoice = 0
privateChoice = 0
messageChoice = 0
messageCount = 0
publicMessage = ""
privateMessage = ""
publicList = [""] * 10
privateList = [""] * 10
signature = ""

pkey = pubGen()
n = pkey.n
e = pkey.e
phi = pkey.phi
privKey = privGen(phi, e)

#TODO: REMOVE LATER
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
            publicMessage = input("Enter a message: ")
            publicList[messageCount] = publicMessage
            print("Message encrypted and sent")
            privateMessage = encrypt(publicMessage, e, n)
            privateList[messageChoice] = privateMessage
            messageCount+=1
            
        if publicChoice == 2:
            if signature is None:
                print("There are no signature to authenticate")
            else:
                print("The following messages are available: ")
                for x in range(messageCount):
                    print(x + 1, ". ", signature)
                    #MORE CODE HERE
        
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
                for x in range(messageCount):
                    print(x + 1, ". (Length = ", len(privateList[x], ")"))
                
                messageChoice = int(input("Enter your choice: "))
                
                if messageChoice == 1:
                    de = decrypt(privateMessage, privKey, n)
                    print("Decrypted message: ", de)
                    
                
        if privateChoice == 2:
            privateMessage = input("Enter a message: ")
            #CODE HERE
            print("Message signed and sent")
            
        if privateChoice == 3:
            userType = 0
                
    if userType == 3:
        break