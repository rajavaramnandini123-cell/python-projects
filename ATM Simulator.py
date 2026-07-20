balance=1000
while True:
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Balance:",balance)
    elif choice==2:
        amount=int(input("enter the deposit amount:"))
        balance+=amount
        print("amount deposited succesfully!")
    elif choice==3:
        amount=int(input("enter withdraw amount:"))
        if amount<=balance:
            balance-=amount
            print("Amount withdrawn succesfully!")
        else:
            print("insufficient Balance!")
    elif choice==4:
        print("thank you")
        break
    else:
        print("Invalid Choice")   
