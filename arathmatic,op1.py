product=input("enter your product")
items=int(input("enter your item"))
price=int(input("enter your price"))
total=("items*price")
sno=1

product2=input("enter your product")
items2=int(input("enter your items2"))
price2=int(input("enter your price2"))
total2=("items2*price2")
sno2=2

product3=input("enter your product3")
items3=int(input("enter your item3")) 
price3=int(input("enter your price3"))
total3=("items3*price3")
sno3=3


product4=input("enter your product4")
items4=int(input("enter your item4"))
price4=int(input("enter your price4"))
total4=("items4*price4")
sno4=4
totalamt=("price*items+price2*items2+price3*items3+price4*items4")

print("------------------------------------------------")
print("|sno| prodect | price | item | totalprice | ")
print("------------------------------------------------")
print("|",sno,"|",product,"   |  ",price," |  ",items," | ",price*items,"  |")
print("|",sno2,"|",product2,"  |  ",price2," |  ",items2," | ",price2*items2,"  |")
print("|",sno3,"|",product3," |  ",price3," |  ",items3," | ",price3*items3,"  |")
print("|",sno4,"|",product4,"    |  ",price4," |  ",items4," | ",price4*items4,"  |")
print("------------------------------------------------")
print("total"  "                        | ",price*items+price2*items2+price3*items3+price4*items4," |" )
print("------------------------------------------------")