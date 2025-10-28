# for i in range(10,0,-1):
#     print(i)

# list1 = [1,2,3,4,6,7,8,87,6]

# print([i for i in list1 if i%2==0])
# for i in list1:
#    if i%2==0:
#        print(i)

##1
# for a in range(20):
#     if a%2==0:
#         print(a+2)



##2
# for b in range (3,0,-1):
#     print(b)


# #3
# count=0

# for a in range(20,100):

#     if a%7==0:
#         count=count+1
# print(count)

##4
# a=int (input('enter the number (1-10)'))
# no =0
# for b in range(0,10):
#     no+=1
#     print(a,'*',no,"=",no*a)

##5
# a=int (input ('enter the number '))
# for i in range (0,a):
#     a+=1
#     print("*")

# #6
# a = int (input ( 'enter the number (2-10)'))
# b=""
# for i in range (a):
#     b+="*"
#     print(b)

# #7
# a=int(input ('enter the number '))

# c=a**2
# for i in range (0,c):
#     print('*',end="")

#8
a=int (input ('enter the number'))
c=a**2
for i in range (0,c):
    print('*',end="")
    if (i+1)%a==0:
        print('')

# ##9
# name=['sathes','prem','megaladevi','rakshana','vel','sivasankari','iniya','ramya ','kannan','rakeshkumar']
# for i in range(0,len(name)-1):
#     print(name[i])


#10
# name=['sathes','prem','megaladevi','rakshana','vel','sivasankari','iniya','ramya ','kannan','rakeshkumar']
# name2=input ('entr the name')
# status=False
# for i in range(0,len(name)):
#     if name[i]==name2:
#       status=True

# if status==True:
#         print('value is found')
# else:     print('not found')

##11
# name=['sathes','prem','megaladevi','rakshana','vel','sivasankari','iniya','ramya ','kannan','rakeshkumar']
# lent=len(name)
# for i in range (0,lent-1):
#     if len(name[i])>5:
#         print(name[i])
    
##12
name=['sathes','prem','megaladevi','rakshana','vel','sivasankari','iniya','ramya ','kannan','Rakeshkumar']
no=len(name)
for i in range(0,no):
    if (name[i][0])=='r' or (name [i][0])=="R":
        print(name[i])

# #   pattern hollow square 
# a=int (input ('enter the number'))
# c=a**2
# for i in range (0,c):
#      print('*',end="")
#      if (i+1)%a==0:
#          print('')
         