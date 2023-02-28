def login():
    print("\t\t\t\t\t*Authorization*\n")
    acc = int(input("Enter your account number: "))
    pas = input("Enter your password: ")
    authorize(acc, pas)


def authorize(acc, pas):
    global Q
    x = 0
    for i in range(len(account)):
        if acc == account[i] and pas == password[i]:
            x = 1
            Q = i

    if x == 0:
        print("Invalid id or password. Please retry!")
        login()
    else:
        print("Authorized succesfully.")

        if usertype == '1':
         mainmenu()

        else:
            adminmain()


def mainmenu():
    temp = 0
    while (temp == 0):
        print("\t\t\t\t\t*Welcome to User Menu*\n")
        print("[1]-Donate blood ")
        print("[2]-Check availablity")
        print("[3]-Logout")
        choice = input("Enter choice(1 or 2 or 3): ")
        print()
        if choice == '1':
            print(name[Q].capitalize(), end="")
            print(", your blood group is", bloodgroup[Q])
            print("Further detail will be shared to you via message shortly.\n")
            print("\t\t\t\t\t|||  THANK YOU  |||\n")

        elif choice == '2':
            needb = input("Enter the blood group required: ")
            quantity = int(input("Enter the amount required(in units): "))
            print()
            print("Processing.....\n")

            j = 0
            while j <= len(available):
                if available[j] == needb:
                    print("Yes! Required blood is available.")
                    print("Collection date and time will be sent via message.\n")
                    print("\t\t\t\t\t|||  THANK YOU  |||\n")
                    break
                j += 1
            else:
                print("Sorry your requirement doesn't meet.")
                
                

        elif choice == '3':
            temp = 1
            print("\t\t\t\t\t|||  LOGGED OUT  |||\n")
        else:
            break


def adminmain():
    temp = 0
    while (temp == 0):
        print("\t\t\t\t\t*Welcome to Administrator Menu*\n")
        print("[1]-Check availablity")
        print("[2]-Recent Donors")
        print("[3]-Logout")
        choice = input("Enter choice(1 or 2 or 3): ")

        if choice == '1':
            needb = input("Enter the blood group required: ")
            quantity = int(input("Enter the amount required(in units): "))
            print("Processing.....")
            j = 0

            while j <= len(available):
                if available[j] == needb:
                    print("Yes! Required blood is available.")
                    print("\t\t\t\t\t|||  THANK YOU  |||\n")
                    break
                j+=1    
            else:
                print("Sorry your requirement doesn't meet.")
                    

                
                
            print("\t\t\t\t\t|||  THANK YOU  |||\n")

        elif choice == '2':
            print("\t\t\t\t\t|||  List of Recent Donors  |||\n")
            for i in range(len(recentdonors)):
                print(i+1, ".", recentdonors[i], end="      ")
                print(available[i], "\n")
    


        elif choice == '3':
            temp = 1
            print("\t\t\t\t\t|||  LOGGED OUT  |||\n")
        


print("\t\t\t\t\t*Welcome to Blood Bank*\n")
print("[1]-New user ")
print("[2]-Administrator\n")

global usertype
global account
global password
global bloodgroup
global available
global recentdonors

usertype = input("Enter user type(1 or 2): ")
account = [12345]
password = ['xyz19']
bloodgroup = ['o+']
name = ['xyz']
available = ['o+', 'a+', 'b-', 'b+', 'ab+', 'ab-']
recentdonors = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']
if (usertype == '1'):
    tempname = input("Enter your name: ")
    name.append(tempname)
    gender = input("Enter your gender(m or f): ")
    age = int(input("Enter your age: "))

    if age < 18:
        print("Sorry you are not eligible!")
        exit()
    bgroup = input("Enter your blood group: ")
    bloodgroup.append(bgroup)
    dhistory = input("Any disease history(y or n): ")
    if dhistory == "y" or dhistory == "Y":
        print("Please consult with our doctor.")
        exit()

    contact = int(input("Enter your contact number: "))
    account.append(contact)
    print("\nYour account created successfully.\n")
    print("New account number: ", contact)

    passw = tempname+str(age)

    print("Password:", passw)

    
    password.append(passw)
    login()

elif (usertype == '2'):
    login()

else:
    print("Invalid option.")    