# #1
# a = int (input ( 'enter the number :'))

# for k in range (a):
#     for i in range (0,a-k):
#             print(" ",end="")
        
#     for j in range (k+1,0,-1):
#         if j==k+1 or k==a-1 :
#             print('*',end="")
#         else:
#             print(' ',end='')
#     for l in range (2,k+2):
#             if l==k+1 or k ==a-1:
#                 print('*',end="")
#             else:
#                 print(' ',end='')

#     print('')


##2
# r=[7,6,5,4,8,2,1]
# k=13
# status =False
# for i in range (0,len(r)):
#    for j in range (0,i):
#       if  r[i]+r[j]==k:
#          print([i],'+',[j],'=',k)
      
# r=[7,6,5,4,8,2,1]
# k=13
# for i in range (0,len(r)):
#    for j in range (0,i):
#       if  r[i]+r[j]==k:
#          print(r[i],'+',r[j],'=',k)
      

##3
v='tan'
o='nat'
l=[i for i in v]
l1=[i for i in o]
l.sort()
l1.sort()
print(l)
print(l1)
if l==l1:
    print('yes')
else:print('noop')

