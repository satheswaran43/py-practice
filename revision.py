a=int(input('enter age'))
if a<18 and a>0:
    print("minor")
elif a<=0:
    print('invalid')
elif a>=18 and a<=60:
    print("major")
elif a>60 and a<=120:
    print("senior citzen")
else:
    print("invalid")
