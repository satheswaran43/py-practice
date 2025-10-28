name=input("enter your name")
a=int (input('enter num'))
b=int (input('enter num'))
 
if name=='+':
    print('plus',a+b)

elif name=='-':
    print('sub',a-b) 

elif name=='/':
    print("div",a/b)   

elif name=='*':
    print('mult',a*b)

elif name=='%':
    print("modlu",a%b)

elif name=='**':
    print('squre', a**2,b**2)

elif name=='//':
    print('no_point',a//b)

else:
    print("no valid signs")