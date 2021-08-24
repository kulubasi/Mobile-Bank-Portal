import re
from os import system

def home():
    ast='O'
    print(ast*60)
    print('               SULULABA MOBILE BANK')
    print(ast*60)
    
def menu_eng():
    print('1.Deposit','\n2.My account','\n3.Cash Withdraw','\n4.Check balance','\n5.More services','\n6.Exit')
    #print('1.Cash Withdraw')
    #print('2.Check balance')
    #print('3.My account')
    #print('4.More services')
def pic():
    print("       __    ___               ___          __  ___  ___  ___   ___                ")
    print("|     /  \  /      | |\   |   /     |   |  /   |    /    /     |    |   | |    |   ")
    print("|    |    | |      | | \  |   \___  |   | |    |___ \___ \___  |__  |   | |    |   ")
    print("|    |    | |  _   | |  \ |       \ |   | |    |        \    \ |    |   | |    |   ")
    print("\___  \__/  \___\  | |   \|    ___/ |___|  \__ |___  ___/  __/ |    |___| |___ |___")



myacno=3200596543
myno="0786808231"
bal=0

trials=[1,2,3]
times=3
transact=[]


while True:
    home()
    print('\n WELCOME TO SULULABA MOBILE BANK','\n\n1.English','\n2.Luganda','\n3.Kiswahili','\n4.Lugbarati')
    lang=input('\nselect language: ')
    #ystem('cls')
        
    if lang =="1":
        home()
        for trial in trials:
            system('cls')
            home()
            password=input("\nEnter your mobile banking PIN: ")
            if password=="1234":
                system('cls')
                pic()
                input("\n\nPress Enter key to continue")
                system('cls')
                while True:
                    home()
                    #print('1.Deposit','\n2.My account','\n3.Cash Withdraw','\n4.Check balance','\n5.More services','\n6.Exit')
                    menu_eng()
                    opt=input('\nselect option:')
                    if opt=="1":
                        amot=int(input("\nEnter amount to deposit:"))
                        bal+=amot
                        newba="Dear customer, you have deposited shs {}".format(amot)
                        transact.append(newba)
                        print(newba)
                        input("Press Enter key to continue")
                        system('cls')
                    elif opt=="2":
                        system("cls")
                        home()
                        print("1.Previous transactions",'\n2.My number','\n0.Main menu')
                        opt4=input("Select option:")
                        if opt4=="1":
                            system("cls")
                            if len(transact)>=1:
                                print(transact[-1])
                                input("Press any key to continue")
                                system('cls')
                                        
                            else:
                                print("There are no previous transactions")
                                input("Press any key to continue")
                                system('cls')
                        elif opt4=='2':
                            system('cls')
                            print("Your current Tariff plan is: \n\t\tMobile/Agent Banking\n\t\tVISA Debit or Credit \n\nYour account number is {}".format(myacno))
                            input("Press any key to continue")
                            system('cls')
                        elif opt4=='0':
                            system('cls')
                            continue
                        else:
                            print('Invalid request')
                            input("Press any key to continue")
                            system('cls')
                    elif opt=="3":
                        try:
                            amt=int(input("Enter amount to withdraw: "))
                            if amt<bal:
                                bal-=amt
                                withdrw="You have withdrawn shs {}".format(amt)
                                transact.append(withdrw)
                                print(withdrw)
                                input("Press Enter key to continue")
                                system('cls')
                            elif amt>=bal:
                                print("Dear customer you have insufficient funds")
                                input("Press Enter key to continue")
                                system('cls')
                            else:system('cls')
                        except ValueError:
                            print("invalid input")
                            input("Press Enter key to continue")
                            system('cls')
                    elif opt=="4":
                        print("Your current balance is {}/=".format(bal))
                        input("Press Enter key to continue")
                        system('cls')
                                
                                        
                                        
                                
                    elif opt=="5":
                        system('cls')
                        print ("\n1.Transfer to another account\n2.Transfer to mobile wallet\n0.Main menu")
                        trans=input("Select option:")
                        if trans =='1':
                            system('cls')
                            try:
                                epin=str(input("Enter other account number:"))
                                system('cls')
                                if len(epin)==10 and re.search(r"\d{10}",epin):
                                    print("\n1.From account no {}".format(myacno))
                                    acc=input("\nSelect option:")
                                    if acc=="1":
                                        system('cls')
                                        print("Enter amount to pay \n(between UGX 5000 and UGX 4000000)")
                                        print("Account balance: UGX {}".format(bal))
                                        acc=int(input("Enter amount to send:"))
                                        system('cls')
                                        print("\nYou are about to send {}/= to {}".format(acc,epin))
                                        print("\n\n1.Confirm\n2.Cancel")
                                        c=input("\nSelect option:")
                                        if c=='1':
                                            if acc>=5000:
                                                if acc<bal:
                                                    system('cls')
                                                    bal-=acc
                                                    print("\nYou have initiated {} from Overdraft {}".format(acc,myacno))
                                                    sen="Sent Cash of UGX{} to account no {} ".format(acc,epin)
                                                    transact.append(sen)
                                                    print(sen)
                                                    print("Your account balance is  UGX {}".format(bal))
                                                    input("Press any key to continue")
                                                    system('cls')
                                                else:
                                                    print("You have insufficient funds:")
                                                    input("Press any key to continue")
                                                    system('cls')
                                            else:
                                                print("Amount cant be sent")
                                                input("Press any key to continue")
                                                system('cls')
                                        elif c =='2':
                                            pass
                                            system('cls')
                                        else:system('cls')
                                    else:system('cls')
                                                                
                                else:
                                    print("Enter 10 digit account number")
                                    input("Press any key to continue")
                                    system('cls')
                            except:
                                print("Unable to carryout transaction Please try again later")
                                input("Press any key to continue")
                                system('cls')
                        elif trans =='2':
                            system('cls')
                            try:
                                print("\n\n1.Transfer to own wallet\n\n2.Transfer to other wallet")
                                wall=str(input("\n\nSelect option:"))
                                if wall=='1':
                                    system('cls')
                                    print("\n\n1.From Overdraft {}".format(myacno))
                                    acco=input("\nSelect option:")
                                    if acco=="1":
                                        system('cls')
                                        print("Enter amount to pay \n(between UGX 5000 and UGX 4000000)")
                                        print("Account balance: UGX {}".format(bal))
                                        tra=int(input("Enter amount:"))
                                        system('cls')
                                        print("\nTransaction Details\nFrom: Overdraft {} \nTo Consumer: {} \n Amount: {}".format(myacno,myno,tra))
                                        print("\n\n1.Confirm\n2.Cancel")
                                        coi=input("\nSelect option:")
                                        if coi=='1':
                                            system('cls')
                                            if tra<bal:
                                                if tra>=5000:
                                                    bal-=tra
                                                    print("You have initiated UGX {} from overdraft{} \n Your account balance is {}".format(tra,myacno,bal))
                                                    senu="\nCash deposit of {}/= to no {} ".format(tra,myno)
                                                    transact.append(senu)
                                                    print(senu)
                                                    input("Press Enter key to continue")
                                                    system('cls')
                                                else:
                                                    print("Amount cant be transferred")
                                                    input("Press Enter key to continue")
                                                    system('cls')
                                            else:
                                                print("You have insufficient funds:")
                                                input("Press Enter key to continue")
                                                system('cls')
                                        elif coi =='2':
                                            pass
                                            system('cls')
                                        else:system('cls')
                                    else:system('cls')
                                elif wall=="2":
                                    system('cls')
                                    print("1.MTN Wallet \n2.AIRTEL Wallet \n3.AFRICELL Wallet")
                                    coi=input("\nSelect option:")
                                    if coi =="1"or"2"or"3":
                                        system('cls')
                                        print("\n\n1.From Overdraft {}".format(myacno))
                                        couio=input("\n\nSelect Option:")
                                        if couio =='1':
                                            system('cls')
                                            pnoo=str(input("\n\nEnter phone contact:"))
                                            if len(pnoo)==10 and re.search(r"\d{10}",pnoo):
                                                system('cls')
                                                print("Enter amount to pay \n(between UGX 500 and UGX 1000000")
                                                print("Account balance: UGX {}".format(bal))
                                                coui=int(input("\n\nEnter Amount:"))
                                                if coui<bal:
                                                    if coui>=500:
                                                        system('cls')
                                                        bal-=acc
                                                        tr="\nCash deposit of {}/= to no {} from Overdraft {}".format(coui,pnoo,myacno)
                                                        print("Your account balance is  UGX {}".format(bal))
                                                        transact.append(tr)
                                                        print(tr)
                                                        input("Press Enter key to continue")
                                                        system('cls')
                                                    else:
                                                        print("Amount cant be transferred")
                                                        input("Press Enter key to continue")
                                                        system('cls')
                                                else:
                                                    print("Insufficient balance")
                                                    input("Press Enter key to continue")
                                                    system('cls')
                                            else:
                                                print("Enter a 10 digit phone number")
                                                input("Press Enter key to continue")
                                                system('cls')
                                        else:
                                            print("Invalid request")
                                            input("Press Enter key to continue")
                                            system('cls')
                                    else:
                                        print("Invalid request")
                                        input("Press Enter key to continue")
                                        system('cls')
                                else:
                                    print("Invalid request")
                                    input("Press Enter key to continue")
                                    system('cls')
                                                        
                            except:
                                print("Unable to carryout transaction Please try again later")
                                input("Press any key to continue")
                                system('cls')
                                                            
                        elif trans=='0':
                            system('cls')
                            continue
                        else:
                            print("Invalid request")
                            input("Press any key to continue")
                            system('cls')
                    
                    elif opt=="6":
                        system('cls')
                        print ("\n\nTHANKYOU FOR USING OUR SERVICE\n\n")
                        input("Press any key to continue")
                        quit()
                    else:
                        print("invalid input")
                        input("Press Enter key to continue")
                        system('cls')
            elif password !="1234":
                times-=1
                system('cls')
                home()
                print("You are remaining with {} attempts".format(times))
                input("Press Enter key to continue")
                #system('cls')
                #if password!="1234" and attempts=='4':
                if password!="1234" and times==0:
                    system('cls')
                    print('Your account has been currently locked, Please try again later')
                    input("Press Enter key to continue")
                    quit()
                
    elif lang=='2':
        system('cls')
        home()
        print("We are still verifying Luganda language")
        input("Press Enter key to continue")
        system('cls')
    elif lang=="3":
        system('cls')
        home()
        print("We are still verifying kiswahili language")
        input("Press Enter key to continue")
        system('cls')
                    
                    
    elif lang=="4":
        system('cls')
        home()
        print("We are still verifying lugbarati language")
        input("Press Enter key to continue")
        system('cls')
    else:
        print("invalid input")
        input("Press Enter key to continue")
        system('cls')

            
                



k=input("Press enter key to exit")

