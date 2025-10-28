x=input('enter ch')
if x in 'aeiouAEIOU' :
    print('veovles')

elif x in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
    print('alpha')

elif x>='0' and x<='9':
    print("number")
    

else:
    print("special ch")