#ATM SIMULATION

#BANK DATABASE

Users={
    10000000001:{'Name':'Shivansh Sharma','Pin':5477,'Balance':82822,'Transactions':[]},
    10000000002:{'Name':'Payal Sharma','Pin':7382,'Balance':72400,'Transactions':[]},
    10000000003:{'Name':'Ayush Rana','Pin':2728,'Balance':54470,'Transactions':[]},
    10000000004:{'Name':'Shivam Sharma','Pin':8332,'Balance':54900,'Transactions':[]},
    10000000005:{'Name':'Rohit Rana','Pin':2722,'Balance':400,'Transactions':[]},
    10000000006:{'Name':'Yuvraj Sharma','Pin':9021,'Balance':6200,'Transactions':[]},
    10000000007:{'Name':'harsh Sharma','Pin':1827,'Balance':9400,'Transactions':[]},
    10000000008:{'Name':'Ishita Sharma','Pin':1477,'Balance':2100,'Transactions':[]},
    10000000009:{'Name':'Harshit Chauhan ','Pin':9457,'Balance':54045,'Transactions':[]},
    10000000010:{'Name':'Varun Kumar','Pin':8877,'Balance':52800,'Transactions':[]},
    10000000011:{'Name':'Dhruv Rana','Pin':5321,'Balance':53320,'Transactions':[]},
    10000000012:{'Name':'Gaurav Kumar','Pin':3822,'Balance':1982,'Transactions':[]},
    10000000013:{'Name':'Raghav Sharma','Pin':7879,'Balance':1189,'Transactions':[]},
    9816054901:{'Name':'Rakesh Kumar Sharma','Pin':5477,'Balance':12200,'Transactions':[]},
    10000000014:{'Name':'Arushi Rana ','Pin':2921,'Balance':935737,'Transactions':[]}
}

current_user=None


#USER LOGIN 
 
def login_user():
    global current_user
    print("                     \nLOGIN OR SIGN IN\n                      ")

    attempts=3
    
    for  i in range(attempts):
        account_num=int(input("Enter account number : "))
        
        pin=int(input("Enter PIN : "))

        if account_num in Users and Users[account_num]['Pin'] == pin:
            print("Logined Successfully ")
            current_user = account_num
            atm_menu()
            break
        else:
            print("Invalid Credentials ! ")
            print("Attempts remaining",attempts - i - 1)

    print("\nAccount Locked,Try again after sometime")
    
    input("\nPress Enter to return to login page.\n")
    return


        
    
#DISPLAY BALANCE

def display_balance():
    print("                     \nDISPLAY BALANCE\n                     ")

    attempts=3

    for i in range(attempts):
        pin=int(input("Enter Pin: "))

        if pin == Users[current_user]['Pin']:
            print("\nYour current balance is",Users[current_user]['Balance'],"₹\n")
            break
        else:
            print("Invalid Credentials ")
            print("Attempts remaining",attempts-i-1)
            
        if i == 3:
            print("\nAccount Locked,Try again in few hours\n")

    input("\nPress Enter to return to menu....\n")
    return


#WITHDRAW MONEY

def withdraw_money():
        print("                     \nWITHDRAW MONEY\n                      ")

        attempts=3

        for i in range(attempts):
            withdraw=int(input("Enter amount: "))
            pin=int(input("Enter Pin to confirm: "))

            if pin == Users[current_user]['Pin']:         
                if  withdraw <= Users[current_user]['Balance']:
                    Users[current_user]['Balance'] -= withdraw
                    print("\nAmmount succefully deducted",withdraw,"₹\n")
                    Users[current_user]['Transactions'].append(f'Withdraw:-{withdraw}')
                    break
                else:
                    print("Insufficient Balance:")
                    break

            else:
                print("Invalid Credentials ")
                print("Remaining attempts",attempts-i-1)

            i+=1
            if i == 3:
                print("\nAccount Locked,Try again in few hours.\n")
        
        input("\nPress Enter to retun to menu....\n")
        return

#DEPOSITE MONEY

def deposit_money():
    print("                     \nDEPOSIT MONEY\n                      ")

    attempts=3

    for i in range(attempts):
        deposit=int(input("Enter amount: "))
        pin=int(input("Enter Pin: "))

        if pin==Users[current_user]['Pin']:
            Users[current_user]['Balance'] += deposit
            print("Amount succesfully added",deposit,"₹")
            Users[current_user]['Transactions'].append(f'Deposit:+{deposit}')
            break
        else:
            print("Invalid Credentials ")
            print("Remaning attempts",attempts-i-1)

        i+=1
        
        if i == 3:
            print("\nAccount Locked,Try again after in few hours.")
    
    input("\nPress Enter to return to menu....\n")
    return



#TRANSACTION RECORD

def transaction_record():
    print("                     \nTRANSACTION HISTORY\n                    ")
    if not Users[current_user]['Transactions']:
        print("No transacations yet")
    else:
        for t in Users[current_user]['Transactions']:
            print(t)
    
    input("\nPress Enter to return to menu....\n")
    return


#   MAIN MENU

def  atm_menu():
    
    while True:
        print('                     \nMAIN MENU\n                     ')
        print("1) Display Balance ")
        print("2) Withdraw Money ")
        print("3) Deposite Money ")
        print("4) Transaction Record ")
        print("5) EXIT ")

        choice=int(input("Enter your choice : "))
            
        if choice == 1:
            display_balance()
        elif choice == 2:
            withdraw_money()
        elif choice == 3:
            deposit_money()
        elif choice == 4:
            transaction_record()
        elif choice == 5:
            print("Thankyou for Trusting us")
            return
        else:
            print("INVALID OPTION ! ")

login_user()
