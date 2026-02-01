

import datetime

#Check if the provided username and password match the administrator's credentials
def login_admin(username,password):
    id="admin"
    passs="password"
    if id == username and passs == password:
        return True


#Register a new staff member with their information.
def new_staff_registaion(name,phone,address,staff_id,username,password):
    staff_info = {
        "Name": name,
        "Phone": phone,
        "Address": address,
        "staff_id": staff_id,
        "Username": username,
        "Password": password
    }
    with open("staff.txt", "r") as file:
        for line in file:
            if username in line:
                print("\n\033[4m" + "Username already exists. Please choose another."+ "\033[0m\n")
                return
            if staff_id in line:
                print("\n\033[4m" + "Staff_Id already exists. Please choose another."+ "\033[0m\n")
                return
    file=open("staff.txt", "a")
    for key, value in staff_info.items():
        file.write(f"{key}: {value}\n")
    file.write("...................................\n")
    print("\n\033[4m" + "Staff account created successfully"+ "\033[0m\n")


#Update staff member information based on their username.
def update_staff(username):
    file=open("staff.txt", "r")
    lines = file.readlines()

#Iterate through lines to find user with matching username
    for i in range(0, len(lines), 7):
        user_info = {}
        for line in lines[i:i+6]:
            parts = line.strip().split(': ', 1)
            
            key, value = parts
            user_info[key] = value
        
        if user_info["Username"] == username:
            print("Name:", user_info["Name"])
            print("Phone:", user_info["Phone"])
            print("Address:", user_info["Address"])
            print("Staff_id:", user_info["staff_id"])
            print("Username:", user_info["Username"])
            print("Password:",user_info["Password"])

            new_name = input("\nEnter new name (press Enter to skip):")
            new_phone = input("Enter new phone number (press Enter to skip):")
            new_address = input("Enter new address (press Enter to skip):")
            new_password = input("Enter new password (press Enter to skip):")

            if new_name:
                lines[i] = f"Name: {new_name}\n"
            if new_phone:
                lines[i+ 1] = f"Phone: {new_phone}\n"
            if new_address:
                lines[i + 2] = f"Address: {new_address}\n"
            if new_password:
                lines[i+5] = f"Password: {new_password}\n"

            # Write updated information back to the file
            with open("staff.txt", "w") as file:
                file.writelines(lines)

            return True
    return False


#View details of a staff member based on their username.
def view_detail_of_staff(username):
    file=open("staff.txt", "r")
    lines = file.readlines()

# Iterate through lines to find user with matching username
    for i in range(0, len(lines), 7):
        user_info = {}
        for line in lines[i:i+6]:
            parts = line.strip().split(': ', 1)
            
            key, value = parts
            user_info[key] = value
        
        if user_info["Username"] == username:
            print("Name:", user_info["Name"])
            print("Phone:", user_info["Phone"])
            print("Address:", user_info["Address"])
            print("Staff_id:", user_info["staff_id"])
            print("Username:", user_info["Username"])
            print("Password:",user_info["Password"],"\n")

            return True
    return False

#################################################################################


#Authenticate staff login credentials.
def login_staff(username, password):
    file = open("staff.txt", "r")
    lines = file.readlines()



# Iterate through lines to find user with matching username
    for i in range(0, len(lines), 7):
        user_info = {}
        for line in lines[i:i + 6]:
            parts = line.strip().split(': ', 1)

            

            key, value = parts
            user_info[key] = value

        if user_info["Username"] == username and user_info["Password"] == password:
            
            print("----------------------------------------------")
            print("\tWelcome", user_info["Name"],"to Staff Account")
            print("----------------------------------------------\n")
            return True
    return False


# Register a new customer with their information.
def new_customer_registaion(name,phonenumber,address,account_number,password,account_type,balance):
    customer_info = {
        "Name": name,
        "Phone_number": phonenumber,
        "Address": address,
        "Account_number": account_number,
        "Password": password,
        "Account_type": account_type,
        "Balance": balance
    }

    file=open("customer.txt", "a")
    for key, value in customer_info.items():
        file.write(f"{key}: {value}\n")
    file.write("...................................\n")


# Update customer information based on their account number.
def update_customer_info(account_number):
    file=open("customer.txt", "r")
    lines = file.readlines()

# Iterate through lines to find user with matching username
    for i in range(0, len(lines), 8):
        user_info = {}
        for line in lines[i:i+7]:
            parts = line.strip().split(': ', 1)
            
            key, value = parts
            user_info[key] = value
        
        if user_info["Account_number"] == account_number:
            print("\nName:", user_info["Name"])
            print("Phone_number:", user_info["Phone_number"])
            print("Address:", user_info["Address"])
            print("Account_type:", user_info["Account_type"])
            print("Password:",user_info["Password"])

            
            new_phone = input("\nEnter new phone number (press Enter to skip):")
            new_address = input("Enter new address (press Enter to skip):")
            new_password =input("Enter new password(press Enter to skip):")
            
            if new_phone:
                lines[i+ 1] = f"Phone_number: {new_phone}\n"
            if new_address:
                lines[i + 2] = f"Address: {new_address}\n"
            if new_password:
                lines[i + 4] = f"Password: {new_password}\n"

            # Write updated information back to the file
            with open("customer.txt", "w") as file:
                file.writelines(lines)
            return True
    return False


#View details of a customer based on their account number.
def view_detail_of_customer(account_number):
    file=open("customer.txt", "r")
    lines = file.readlines()

# Iterate through lines to find user with matching username
    for i in range(0, len(lines), 8):
        user_info = {}
        for line in lines[i:i+7]:
            parts = line.strip().split(': ', 1)
            
            key, value = parts
            user_info[key] = value
        
        if user_info["Account_number"] == account_number:
            print("\nName:", user_info["Name"])
            print("Phone_number:", user_info["Phone_number"])
            print("Address:", user_info["Address"])
            print("Account_type:", user_info["Account_type"])
            print("Password:",user_info["Password"])

            return True
    return False


#################################################################################


#Authenticate customer login credentials.
def login_customer(username,password):
    file=open("customer.txt","r")
    lines=file.readlines()


    for i in range(0, len(lines), 8):
        user_info = {}
        for line in lines[i:i+7]:
            parts = line.strip().split(': ', 1)
            
            key, value = parts
            user_info[key] = value
        
        if user_info["Account_number"] == username and user_info["Password"]== password:
            
            print("--------------------------------------")
            print("\tWelcome",user_info["Name"])
            print("--------------------------------------")
            return True
    return False
def password_check(username,password):
    file=open("customer.txt","r")
    lines=file.readlines()


    for i in range(0, len(lines), 8):
        user_info = {}
        for line in lines[i:i+7]:
            parts = line.strip().split(': ', 1)
            
            key, value = parts
            user_info[key] = value
        
        if user_info["Account_number"] == username and user_info["Password"]== password:
            return True
    return False


#Update the password of a customer based on their username.
def update_customer_password(new_password,username):
    file=open("customer.txt", "r")
    lines = file.readlines()

# Iterate through lines to find user with matching username
    for i in range(0, len(lines), 8):
        user_info = {}
        for line in lines[i:i+7]:
            parts = line.strip().split(': ', 1)
            
            key, value = parts
            user_info[key] = value
        
        if user_info["Account_number"] == username:
            lines[i + 4] = f"Password: {new_password}\n"
            with open("customer.txt", "w") as file:
                file.writelines(lines)
                return True
    


#Deposit funds into a customer's account and update their balance.
def customer_deposit(deposit,account_number):
    file=open("customer.txt", "r")
    lines = file.readlines()

# Iterate through lines to find user with matching username
    for i in range(0, len(lines), 8):
        user_info = {}
        for line in lines[i:i+7]:
            parts = line.strip().split(': ', 1)
            
            key, value = parts
            user_info[key] = value
        
        if user_info["Account_number"] == account_number:
            balance= int(user_info["Balance"])
            new_balance=balance+deposit
            lines[i + 6]= f"Balance: {new_balance}\n"

            with open("customer.txt", "w") as file:
                file.writelines(lines)

            transaction_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            statement_info={
                "Account_number": account_number,
                "Time": transaction_time,
                "Amount_deposited": deposit

            }
            file=open("statement.txt","a")
            for key, value in statement_info.items():
                file.write(f"{key}: {value}\n")
            file.write("...................................\n")
            return True
    
#Withdraw funds from a customer's account and update their balance.
def customer_withdrawal(withdrawal,account_number):
    file=open("customer.txt", "r")
    lines = file.readlines()

# Iterate through lines to find user with matching username
    for i in range(0, len(lines), 8):
        user_info = {}
        for line in lines[i:i+7]:
            parts = line.strip().split(': ', 1)
            
            key, value = parts
            user_info[key] = value
        
        if user_info["Account_number"] == account_number:
            account_type=user_info["Account_type"]
            balance= int(user_info["Balance"])
            check=balance-withdrawal

            if account_type=="saving account":
                if check>100:
                    new_balance=balance-withdrawal
                    lines[i + 6]= f"Balance: {new_balance}\n"   
                else:
                    print('''\nThe minimum balance of for saving account is Rs 100
and this transaction will lead minimum balance to be below Rs 100''')
                    print("\nYour balance is",balance)
                    return False
            elif account_type=="current account":
                if check>499:
                    new_balance=balance-withdrawal
                    lines[i + 6]= f"Balance: {new_balance}\n"
                else:
                    print('''\nThe minimum balance of for current account is Rs 500
and this transaction will lead minimum balance to be below Rs 500''')
                    print("\nYour balance is",balance)
                    return False
                    
                with open("customer.txt", "w") as file:
                        file.writelines(lines)
                transaction_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                statement_info={
                    "Account_number": account_number,
                    "Time": transaction_time,
                    "Amount_withdrawal": withdrawal
                }
                file=open("statement.txt","a")
                for key, value in statement_info.items():
                    file.write(f"{key}: {value}\n")
                file.write("...................................\n")
                return True

def account_check(account_number):
    file=open("customer.txt", "r")
    lines = file.readlines()

# Iterate through lines to find user with matching username
    for i in range(0, len(lines), 8):
        user_info = {}
        for line in lines[i:i+7]:
            parts = line.strip().split(': ', 1)
            
            key, value = parts
            user_info[key] = value
        
        if user_info["Account_number"] == account_number:
            return True
    print("\n Account with account number", account_number,"not found.")
    return False

    

def statement(account_number, start_date, end_date):
    file = open("customer.txt", "r")
    lines = file.readlines()
    balance = 0
    total_withdrawal=0
    total_deposited=0
    # Iterate through lines to find user with matching username
    for i in range(0, len(lines), 8):
        user_info = {}
        for line in lines[i:i + 7]:
            parts = line.strip().split(': ', 1)
            key, value = parts
            user_info[key] = value

        if user_info["Account_number"] == account_number:
            balance = int(user_info["Balance"])

    file = open("statement.txt", "r")
    lines = file.readlines()
    # Iterate through lines to find user with matching username
    for i in range(0, len(lines), 4):
        user_info = {}
        for line in lines[i:i + 3]:
            parts = line.strip().split(': ', 1)
            key, value = parts
            user_info[key] = value

        transaction_time = datetime.datetime.strptime(user_info["Time"], "%Y-%m-%d %H:%M:%S")

        if user_info["Account_number"] == account_number and start_date <= transaction_time <= end_date:
            if "Amount_deposited" in user_info:
                print("\nAmount_deposited-------------------", user_info["Amount_deposited"])
                
                total_deposited=int(user_info["Amount_deposited"])+total_deposited
            if "Amount_withdrawal" in user_info:
                print("\nAmount_withdrawal------------------", user_info["Amount_withdrawal"])
                
                total_withdrawal=int(user_info["Amount_withdrawal"])+total_withdrawal
            print("Time:", user_info["Time"])
            print("---------------------------------------------------------------------\n")
    if balance==0:
        print("\nAccount number not Found")
    else:
        print("\nFinal balance:", balance)
        print("Total deposited:-",total_deposited)
        print("Total withdrawal:-",total_withdrawal)
    return


def first_login(username,password):
    file=open("customer.txt","r")
    lines=file.readlines()
    
    


    for i in range(0, len(lines), 8):
        user_info = {}
        for line in lines[i:i+7]:
            parts = line.strip().split(': ', 1)
            
            key, value = parts
            user_info[key] = value

        
        if user_info["Account_number"] == username:
            defaultpassword="password"+user_info["Phone_number"]
            if defaultpassword==password:
                return True
    return False
###################################################################################
staff_info = {}

customer_info ={}

statment_info={}

file=open("customer.txt","a")
file.close()
file=open("staff.txt","a")
file.close
file=open("statement.txt","a")
file.close

while True:  
    #to display the front menu
    print("----------------------------------------------------------") 
    print("\t Welcome to the Login Page of Prime Bank")
    print("----------------------------------------------------------")
    print("1. Login")
    print("2. Register")
    


#to take input of the choice
    choice_in_login_page=(input("\nEnter your choice:-"))


    if choice_in_login_page=="1":
        print("\nEnter your login Username and Password")
        username=input("Username:")
        password=input("Password:")



        if login_admin(username,password):
            while True:
# to update staff_accounts or customer_account
                print("\n----------------------------------------")
                print("\tWelcome to Admin Account")
                print("----------------------------------------\n")
                print("1. To add 'Staff Account'")
                print("2. To update 'Staff Account'")
                print("3. To view 'Staff details'")
                print("4. To view 'Customer details'")
                print("5. To update 'Customer Account'")
                print("6. To view statement of cusotmer")
                print("7. To logout\n")
                choice_for_wether_to_update_or_view=(input("Enter your choice:-"))
            

                if choice_for_wether_to_update_or_view=="1":
                    
                    print("\n\033[4m" + "Inorder to add new staff account plz fill the form below"+ "\033[0m\n")
                    name = input("Enter the name: ")
                    phone = input("Enter the phone number: ")
                    address = input("Enter the address: ")
                    staff_id= input("Enter the staff_id: ")
                    username = input("Enter a username: ")
                    password = input("Enter a password: ")
                    new_staff_registaion(name,phone,address,staff_id,username,password)

                elif choice_for_wether_to_update_or_view=="2":
                    username=(input("\nEnter the staff's username you want to update:-"))
                    if update_staff(username):
                        
                        print("\n\033[4m" + "Updated succefully"+ "\033[0m\n")
                    else:
             
                        print("\n\033[4m" + "Staff with username",username," not found."+ "\033[0m\n")


                elif choice_for_wether_to_update_or_view=="3":
                    print("\n1. To view all staff's info")
                    print("2. To view specific staff's info")

                    choice_to_view_staff_info=(input("\nEnter the number:-"))
                    if choice_to_view_staff_info=="1":
                        file=open("staff.txt","r")
                        print(file.read())
                        file.close()
                    
                    elif choice_to_view_staff_info=="2":
                        username=(input("\nEnter the staff's username you want to view detail of: "))
                        if view_detail_of_staff(username):
                            print()
                        else:
                            print("\nStaff with username",username," not found.")
                    else:
                    
                        print("\n\033[4m" + "Invalid choice"+ "\033[0m\n")
                        
                
                elif choice_for_wether_to_update_or_view=="4":

                    print("\n1. To view all customer's info")
                    print("2. To view specific customer's info")

                    choice_to_view_customer_info=(input("\nEnter the number:-"))
                    if choice_to_view_customer_info=="1":
                        file=open("customer.txt","r")
                        print(file.read())
                        file.close()
                    
                    if choice_to_view_customer_info=="2":
                        account_number=(input("\nEnter the account number you want to view detail of: "))
                        if view_detail_of_customer(account_number):
                            print()
                            
                        else:
                            print("\n\033[4m" + "Account with account number",account_number,"not found"+ "\033[0m\n")


                elif choice_for_wether_to_update_or_view=="5":
                    account_number=(input("\nEnter the account number of the customer that you want to update:-"))
                    if update_customer_info(account_number):
                        print("\n\033[4m" + "Updated sucessfully!!"+ "\033[0m\n")

                    else:
                        print("\n\033[4m" + "Account with account number",account_number,"not found"+ "\033[0m\n")
                
                elif choice_for_wether_to_update_or_view=="6":
                    account_number=input("\nEnter the account number of the customer:-")
                    try:
                        start = input("\nEnter start date (YYYY-MM-DD): ")
                        start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
                        end = input("Enter end date (YYYY-MM-DD): ")
                        end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
                        end_date = end_date + datetime.timedelta(days=1) - datetime.timedelta(seconds=1)
                        statement(account_number, start_date, end_date)
                    except ValueError:
                        print("\n\033[4m" + "Invalid date format. Please enter the date in the format YYYY-MM-DD."+ "\033[0m\n")
                    
                        
                    
                elif choice_for_wether_to_update_or_view=="7":
                    break
                else:
                    print("\n\033[4m" + "Invalid choice"+ "\033[0m\n")       

#####################################################################################

        elif login_staff(username,password):
            while True:
                
                print("1. To add new customer account")
                print("2. To update customer details")
                print("3. To view customer details")
                print("4. To view customer's statement")
                print("5. To logout")
                
                choice_for_staff_to_add_or_update=(input("\nEnter the number:-"))
                if choice_for_staff_to_add_or_update=="1":
                    print("\n\033[4m" + "Inorder to add new customer plz fill the form given bellow"+ "\033[0m\n")
                    name=input("\nEnter the full name:-")
                    phonenumber=(input("Enter the phone number:-"))
                    address=input("Enter the address:-")
                    password="password"+phonenumber

#to autogenerate account number in sequence
                    
                    file=open("customer.txt","r")
                    lines=file.readlines()

                    account_number_count=1
                    for line in lines:
                        if "Account_number" in line:
                            account_number_count+=1
                    account_number=("{:04d}".format(account_number_count))
                    account_type=input("Enter your account type(current account or saving account):-")
                    if account_type=="saving account":
                        balance=int(100)
                    else:
                        balance=int(500)
                    new_customer_registaion(name,phonenumber,address,account_number,password,account_type,balance)
                    print("\n\033[4m" + "\nThe account number and password for ",name,"is:-"+ "\033[0m\n")
                    print("-------------------------------------")
                    print("\tAccount number:-",account_number)
                    print("\tPassword:-",password)
                    print("-------------------------------------")


                elif choice_for_staff_to_add_or_update=="2":
                    account_number=(input("\nEnter the account number of the customer that you want to update:-"))
                    if update_customer_info(account_number):
                        print("\n\033[4m" + "Updated succefully"+ "\033[0m\n")
                    else:
                        print("-----------------------")
                        print("\n\033[4m" + "Account with account number",account_number,"not found"+ "\033[0m\n")

                elif choice_for_staff_to_add_or_update=="3":
                    print("\n1. To view all customer's info")
                    print("2. To view specific customer's info")

                    choice_to_view_customer_info=(input("\nEnter the number:-"))
                    if choice_to_view_customer_info=="1":
                        file=open("customer.txt","r")
                        print(file.read())
                        file.close()
                    
                    if choice_to_view_customer_info=="2":
                        account_number=(input("\nEnter the account number you want to view detail of: "))
                        if view_detail_of_customer(account_number):
                            print()
                        else:
                            print("\n\033[4m" + "Account with account number",account_number,"not found"+ "\033[0m\n")

                elif choice_for_staff_to_add_or_update=="4":
                    account_number=input("\nEnter the account number of the customer:-")
                    try:
                        start = input("Enter start date (YYYY-MM-DD): ")
                        start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
                        end = input("Enter end date (YYYY-MM-DD): ")
                        end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
                        end_date = end_date + datetime.timedelta(days=1) - datetime.timedelta(seconds=1)
                        statement(account_number, start_date, end_date)
                    except ValueError:
                        print("\n\033[4m" + "Invalid date format. Please enter the date in the format YYYY-MM-DD."+ "\033[0m\n")
                
                elif choice_for_staff_to_add_or_update=="5":
                        break
                else:
                    print("\n\033[4m" + "Invalid choice"+ "\033[0m\n")
    
############################################################################################




        elif login_customer(username,password):   
            while True:           
                if first_login(username,password):

                    print("\nSince you are using the default password, you need to change your password first.")
                    while True:
                        new_password=input(("\nEnter your new password:-"))
                        retype=input("Enter your new password again:-")
                        if new_password==retype:
                            update_customer_password(new_password,username)
                            print("\n\033[4m" + "Successfully Changed Password"+ "\033[0m\n")
                            break
                        else:
                            print("\n\033[4m" + "Passwords donot matches"+ "\033[0m\n")
                    break      
                else:

                    print("\n1. To change password ")
                    print("2. For deposit")
                    print("3. For withdrawal")
                    print("4. For Statement of Account Report")
                    print("5. To transfer funds")
                    print("6. To logout")
                    choice_of_customer=(input("\nEnter the number :-"))
                
                    account_number=username

                    if choice_of_customer=="1":
                        password=input(("\nEnter your current password:-"))
                        if password_check(username,password):
                            new_password=input(("Enter your new password:-"))
                            retype=input("Enter your new password again:-")
                            if new_password==retype:
                                update_customer_password(new_password,username)
                                print("\n\033[4m" + "Successfully Changed Password"+ "\033[0m\n")
                                break
                            else:
                                print("\n\033[4m" + "Passwords donot matches"+ "\033[0m\n")
                        else:
                            print("\n\033[4m" + "Current password donot match"+ "\033[0m\n")

                    elif choice_of_customer=="2":
                        deposit=int(input("\nEnter the amount you want to deposit:-"))
                        customer_deposit(deposit,account_number)
                        print("\n\033[4m" + "Rs",deposit,"has been deposited succefully to your account"+ "\033[0m\n")
                    
                    elif choice_of_customer=="3":
                        withdrawal=int(input("\nEnter the amount you want to withdrawal:-"))
                        if customer_withdrawal(withdrawal,account_number):
                            print("\n\033[4m" + "Rs",withdrawal,"has been deposited succefully to your account"+ "\033[0m\n")
                        else:
                            
                            print("\n\033[4m" + "Withdrawal Failed !!!"+ "\033[0m\n")


                    elif choice_of_customer=="4":
                        account_number=username
                        try:
                            start = input("\nEnter start date (YYYY-MM-DD): ")
                            start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
                            end = input("Enter end date (YYYY-MM-DD): ")
                            end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
                            end_date = end_date + datetime.timedelta(days=1) - datetime.timedelta(seconds=1)
                            statement(account_number, start_date, end_date)
                        except ValueError:
                            print("\n\033[4m" + "Invalid date format. Please enter the date in the format YYYY-MM-DD."+ "\033[0m\n")


                    elif choice_of_customer=="5":
                        account_number=username
                        transfer_account_number=input("\nEnter the reciver's account number:-")
                        amount=int(input("\nEnter the amount you want to transfer:-"))
                        withdrawal=amount
                        deposit=amount

                        if account_check(transfer_account_number):
                            customer_withdrawal(withdrawal,account_number)
                            customer_deposit(deposit,transfer_account_number)
                            print("\nRs",amount,"successfully transfered to account number",transfer_account_number)
                        else:
                            print("\nTransaction fail !!!")



                    elif choice_of_customer=="6":
                            break
                    else:
                        print("\n\033[4m" + "Invalid choice"+ "\033[0m\n")


        else:
            print("\n\033[4m" + "Username and Password not found"+ "\033[0m\n")



    elif choice_in_login_page=="2":
        print("\n\033[4m" + "Inorder to open new account please provide the following information"+ "\033[0m\n")
        name=input("Enter your name:-")
        phonenumber=input("Enter your phone number:-")
        address=input("Enter your address:-")
        age=(input("Enter your age:-"))
        email=input("Enter your email address:-")
        account_type=input("Enter your account type(saving/current account):-")
        customer_detail={
            "Name": name,
            "Phone_number": phonenumber,
            "Address": address,
            "Age": age,
            "Email": email,
            "Account_type": account_type
        }

        file=open("customer_form.txt","a")
        for key, value in customer_detail.items():
            file.write(f"{key}: {value}\n")
        file.write("...................................\n")
        print('''Your information has been saved 
    you can collect your account number and password by contacting our staff members and
    make sure to change your password after your first login''')
        break
    else:
        print("\n\033[4m" + "Invalid choise.Please try again"+ "\033[0m\n")
            
            
                
