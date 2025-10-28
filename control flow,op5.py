pin=int(input("enter your pin"))
if pin==1234:
    print("next")
    withdraw=int(input("enter the amt"))
    balance=9000

    if withdraw<balance:    
        print("collect your cash")

    if withdraw>balance:
        print("influnce blance")

    if withdraw==balance:
        print("collect the cash")

else:
    print("Invalid pin")
