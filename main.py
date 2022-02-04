userType = 0
userChoice = 0
publicChoice = 0
publicMessage = ""

while True:
    print("RSA Keys has been generated")
    print("Please select your user type")
    print("\n1. A public user")
    print("\n2. The owner of the key")
    print("\n3. Exit program")
    userType = input("Enter your choice: ")
    
    if userType == 1:
        print("As a public user, what would you like to do?")
        print("\n1. Send an encrypted message")
        print("\n2. Authenticate a digital signature")
        print("\n3. Exit")
        userChoice = input("Enter your choice: ")
        
        if userChoice == 1:
            publicMessage = input("Enter a message: ")
            print("Message encrypted and sent")
        
    if userType == 2:
        print("As the owner of the keys, what would you like to do?")
        print("\n1. Decrypt a received message")
        print("\n2. Digitally sign a message")
        print("\n3. Exit")
        userChoice = input("Enter your choice: ")
    
    else:
        break