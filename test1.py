qty_rice=int(input('enter the quantity'))
qty_milk=int(input('enter milk'))
amountpaid=int(input('enter amt paid'))

rate1=290.00
rate2=50.0
amount1=rate1*qty_rice
amount2=rate2*qty_milk

print("super market")
print("123,main road,cityville")
print("contact:+91-9876543210")
print('GSTIN27AAAPL1234C1ZV')
print('date:26/06/2025')
print("Bill No:SM1025")

print("---------------------------------")
print("sno | item| qty|  rate | amount|")
print("--------------------------------")
print("1","  |rice","| ",qty_rice,"|",rate1,"|",amount1,"|")
print("2","  |milk","| ",qty_milk,"|",rate2," |",amount2,"|")     
print("-------------------------------")

subtotal=(amount1+amount2)
gst=(18*subtotal)/100
print("subtotal=",subtotal)
print("gst(18)=",gst)
print('ampuntpaid=',amountpaid)
balance=amountpaid-(subtotal+gst)
print("balance=",balance)

print("payment mode:cash")
print("thank you for shopping with us!")
print("visitagain:)")