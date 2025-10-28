m=int(input('enter mark'))
if m>100:
    print('invalid')

elif m==100:
    print('A++')

elif m>90 and m<=99:
    print(('A'))

elif m>80 and m<=90:
    print("B")

elif m>70 and m<=80:
    print('C')

elif m>60 and m<=70:
    print('D')

elif m>50 and m<=60:
    print('E')

else:
    print("fail")