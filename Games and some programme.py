#program:
#Authors: George Malak Magdy
#Version:
#Date: 26/2/2024

invalid_input = False
while True:
    if not invalid_input:
        print("Problem 1, Grade calculator program ")
        print("Problem 2, Checking whether a specific number is armstrong or not ")
        print("Problem 3, Calculation of approximation of PI")
        print("Problem 4, Encryption programme")
        print("Problem 5, Lists Comparative")
        print("Problem 6, Numbers factorial finder")
        print("Exit program press 0 ")
    try:
        pro_num = int(input("Please Enter Your problem number: "))
        if pro_num < 0 or pro_num > 6:
        	raise ValueError
        if pro_num == 1:
            print("Welcome to grade calculator program")
            #handle errors while loop
            while True:
                try:
                    stu_deg = int(input("Please Enter Your Degree: "))
    
                    if 0 <= stu_deg <= 100:
                        if 0 <= stu_deg < 50:
                            print("Your Grade is \"F\"")
                        elif 50 <= stu_deg <= 54:
                            print("Your Grade is \"D-\"")    
                        elif 55 <= stu_deg <= 59:
                            print("Your Grade is \"D\"")
                        elif 60 <= stu_deg <= 63:
                            print("Your Grade is \"D+\"")
                        elif 64 <= stu_deg <= 67:
                            print("Your Grade is \"C-\"")    
                        elif 68 <= stu_deg <= 71:
                            print("Your Grade is \"C\"")
                        elif 72 <= stu_deg <= 75:
                            print("Your Grade is \"C+\"")
                        elif 76 <= stu_deg <= 79:
                            print("Your Grade is \"B-\"")
                        elif 80 <= stu_deg <= 83:
                            print("Your Grade is \"B\"")
                        elif 84 <= stu_deg <= 87:
                            print("Your Grade is \"B+\"") 
                        elif 88 <= stu_deg <= 91:
                            print("Your Grade is \"A-\"")
                        elif 92 <= stu_deg <= 95:
                            print("Your Grade is \"A\"")
                        elif 96 <= stu_deg <= 100:
                            print("Your Grade is \"A+\"")
                        break    
                    else:
                        print("Error, Please Enter Your Degree Correctly (between 0 and 100)")
                except ValueError:
                    print("Error, Please Enter Your Degree as a Number")
                    
        elif pro_num == 2: 
            def programTwo():
                # HEADER
                print('\n############################################')
                print('This program is for checking whether a specific number is armstrong or not.')
                print('############################################\n')

                # GETTING INPUT
                while True:
                    numStr = input('Enter a number: ')
                    try:
                        num = int(numStr)
                        if num < 0:
                            raise
                        break
                    except:
                        print('This is not a vaild non negative integer!\n')

                # CHECKING
                checkNum = 0

                for digit in numStr:
                    checkNum += int(digit) ** len(numStr)
                
                # PRINTING OUTPUT
                if checkNum == num:
                    print(f'\nTrue!\n{numStr} is an armostrong number.\n')
                else:
                    print(f'\nFalse!\n{numStr} is not an armostrong number.\n')

            programTwo() 
          
        elif pro_num == 3:
            # welcome message #
            print("Welcome to calculation of approximation of PI")
            # fun to calculate pi #
            def calculate (terms) :
                pi_sum = 0
                sign = 1
                #calculate it#
                for i in range (1 , terms+1):
                    denominator = (2 * i) - 1
                    term = sign * (1 / denominator)
                    pi_sum += term
                    sign *= -1
                pi = pi_sum * 4
                return pi
            #====Mainprgoram====#
            while True :
                try:
                    terms = int(input(f"Please enter the number of terms which you want : "))
                    if terms <= 0:
                        raise ValueError
                    break
                except:
                	print("Please enter a positive number only!\n")
            result = calculate(terms)
            print(f" Approximation of Pi equal : " , result)
            print (" End of calculation\n")

        elif pro_num == 4:
            # welcome message #
            print("Welcome to Encryption programme")
            # warn message#
            print("Warning: Please ensure that you securely manage your encryption keys! ")
            def encrypt(mess , shift): #fun to encrypt your message#
                final_message = ""
                for i in mess:
                    if i.isalpha():
                        if i.isupper():
                            encrypted_char = chr((ord(i) - 65 + shift) % 26 + 65)
                        else:
                            encrypted_char = chr((ord(i) - 97 + shift) % 26 + 97)
                    else:
                        encrypted_char = i
                    final_message += encrypted_char
                return final_message
            
            def decode (mess , shift) : #fun to decode your encrypted message#
                decoded_message = ""
                for i in mess:
                    if i.isalpha():
                        if i.isupper():
                            encrypted_char = chr((ord(i) - 65 - shift) % 26 + 65)
                        else:
                            encrypted_char = chr((ord(i) - 97 - shift) % 26 + 97)
                    else:
                        encrypted_char = i
                    decoded_message += encrypted_char
                return decoded_message
            #====main prograame===#
            print("Choose from list what you convert to :")
            print("1 - You want to Encrypt your message")
            print("2 - You want to decode your message")
            choice = input("Enter you choice: ")
            while choice != '1' and choice != '2':
                choice = input("Please enter 1 or 2 only from the list: ")
            if choice == '1':
                message = input("Enter your message : ")
                while True:
                	try:
                		shift = int(input("Enter your shift : "))
                		if shift <= 0:
                			raise ValueError
                		break
                	except:
                		print("Please enter positive integers only!\n")
                messencrypts = encrypt(message , shift)
                print("Encrypted message: ", messencrypts, "\n")
            elif choice == '2':
                message = input("Enter your message : ")
                while True:
                	try:
                		shift = int(input("Enter your shift : "))
                		if shift <= 0:
                			raise ValueError
                		break
                	except:
                		print("Please enter positive integers only!\n")
                messdecode = decode(message , shift)
                print("Decoded message: ", messdecode, "\n")
                

        elif pro_num == 5:     
            #function to turn lists into sets to check if lists are equal
            def are_equal(list1, list2):
                set1 = set()
                set2 = set()
                for x in list1:
                    set1.add(x)
                    
                for z in list2:
                    set2.add(z)    
                    
                if set1 == set2:
                    print("lists are equal\n")
                else:
                    print("lists are not equal\n")    
                   
            #assign list1 and list2
            list1 = []
            list2 = []
            #handle errors while loop
            while True:
                try:
                    list1_length =int(input("Welcome, Please insert first list length: "))
                    if list1_length < 0:
                    	raise ValueError
                    list2_length =int(input("Please insert second list length: "))
                    if list2_length < 0:
                    	raise ValueError
                    #check if lists length are equal         
                    if list1_length == list2_length:
                        # input list 1 elements
                        for i in range(list1_length):
                            element1= input("enter element of the first list: ")
                            i=i+1
                            list1.append(element1)
                        print(list1)  
                        print("")
                        # input list 2 elements
                        for i in range(list2_length):
                            element2= input("enter element of the second list: ")
                            i=i+1
                            list2.append(element2)

                        print(list2)   
                        print("")
                        are_equal(list1, list2)
                        break
                    else: 
                       print("lists are not equal\n")
                       break
                except ValueError:
                    print("Error, Please Enter Your List as a Non Negative Numbers Only\n")
                

        elif pro_num == 6:
            def programSix():
                # HEADER
                print('\n############################################')
                print('This program is for getting the factors of a specific number')
                print('############################################\n')

                # GETTING INPUT
                while True:
                    numStr = input('Enter a number: ')
                    try:
                        num = int(numStr)
                        if num <= 0:
                            raise
                        break
                    except:
                        print('This is not a vaild positive integer!\n')
                
                # GETTING FACTORS
                factorsList = []
                
                i = 1
                while i <= num:
                    if num % i == 0:
                        factorsList.append(i)
                    i += 1
                
                # PRINT OUTPUT
                print(f'\nFactors of {num} are {factorsList}!\n')

            programSix()
            

        elif pro_num == 0:
            print("Ending program, Good Bye!")
            print("###########################\n")
            break
        invalid_input = False
        

        
    except ValueError:
        print("Error, This is not a valid choice!") 
        invalid_input = True
  
           
    
            