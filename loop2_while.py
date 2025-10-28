##1

# i=1
# while i<=10:
#     print(i)
#     i+=1


##3
# i=10
# while i>0:
#     print(i)
#     i-=1

# # 3
# p=1
# while p<=20:
#     if p%2==0:
#         print(p)
#     p+=1
    
##4
# a=20
# count=0
# while a<=100:
#     if   a%7==0:
#         count=count+1
#     a+=1
# print(count)

##5
# a=1
# b=int(input('number'))
# while a<=10:
#     c=a*b
#     print(b,"*",a,"=",c)
#     a+=1


##6
# k=1
# l=int(input('number'))
# if l%2==0:
#     while k<=10:
#             m=l*k
   
#             print(k,"*",l,"=",m)
#             k+=1
# k2=10
# if l%2!=0:
#     while k2>=1:
#             k2l=k2*l
#             print(k2,"*",l,"=",k2l)
#             k2-=1



##7
# r=int(input("entr the number "))
# l=''
# i=0
# while i<r:
#     l+="*"
#     i+=1
# print(l)

##8
# r=int(input("entr the number "))
# i=0
# v=r**2
# while i<v:
#     print("*",end="")
#     i+=1

##9
# r=int(input("entr the number "))
# i=1
# v=r**2
# while i<=v:
#     print("*",end="")
#     if i%r==0:
#         print('')
#     i+=1

# #10
# r=int(input("entr the number "))
# i=1
# v=''
# while i<=r:
#         v+="*"
#         print(v)
#         i+=1



##11
# name=['sathes','prem','megaladevi','rakshana','vel','sivasankari','iniya','ramya ','kannan','rakeshkumar']
# number=len(name)
# i=0
# while i<=number:
#     print(name[i-1])
#     i+=1

#12
# name=['sathes','prem','megaladevi','rakshana','vel','sivasankari','iniya','ramya ','kannan','rakeshkumar']
# name2=input('enter the name:')
# nu=len(name)
# status = False
# i=0
# while(i<nu):
#     if name[i] == name2:
#         status=True
#     i+=1
# if status:
#     print("Value is found")
# else:
#     print("value is not found")

#13
name=['sathes','prem','megaladevi','rakshana','vel','sivasankari','iniya','ramya ','kannan','rakeshkumar']
no=len(name)
i=0
while(i<no):
    if len(name[i])>5:
        print(name[i])
    i+=1

#14
# name=['sathes','prem','megaladevi','rakshana','vel','sivasankari','iniya','ramya ','kannan','rakeshkumar']
# no=len(name)
# i=0
# while(i<no):
#     if (name[i][0])=="r" or (name[i][0])=='R':
#         print(name[i])
#     i+=1


# List of numbers
numbers = [1, 2, 3, 4, 5]

# Loop through the list and add 5 to each number
for i in range(len(numbers)):
    numbers[i] += 5

# Print the updated list
print(numbers)
