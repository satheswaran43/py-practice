x=input("enter your name")
age =int(input("age"))

if x=="female" :
    if age>=18 and age<=120:
      print("valid")

    else:
          print("invalid")


elif x=="male":
    if age>=21 and age<=120:
        print('valid')
    else:
        print("invalid age")
else:
      print("invalid gender")
            
                