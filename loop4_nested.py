# t=int(input (''))
# c=t**2
# for i in range (0,c):
#     for j in range (0,c):
#         print('*',end="")
#     print('')

##2
# a = int (input ( 'enter the number :'))
# for i in range (1,a+1):
#     for j in range (0,i):
#         print("*",end="")
#     print('')

# ##3

# t=int(input (''))
# for i in range (0,t):
#     for j in range (0,t):
#         if i==0 or j==0 or i==t-1 or j==t-1 :
#             print('*',end="")
#         else :
#             print(' ',end='')
#     print('')
        
##4
# a = int (input ( 'enter the number :'))
# for i in range (1,a+1):
    # for j in range (1,i+1):
        # print(j,end="")
    # print('')
    # 
##5
# a = int (input ( 'enter the number :'))
# for i in range (0,a+1):
    # for j in range (i,0,-1):
        # print(j,end="")
    # print('')
# 

###### 6

# a = int (input ( 'enter the number :'))
# for k in range (a):
    #  for i in range (0,a-k):
            # print(" ",end="")
    #  for j in range (k+1,0,-1):
            # print(j,end="")
    #  print('')

# #7

# a = int (input ( 'enter the number :'))
# for k in range (a):
    # for i in range (0,a-k):
            # print(" ",end="")
    # for j in range (k+1,0,-1):
            # print(j,end="")
    # for l in range (2,k+2):
        #    print(l,end='')
    # print('')
##8
# a = int (input ( 'enter the number :'))
# for k in range (a,-1,-1):
#     for i in range (0,a-k):
#             print(' ',end="")
#     for j in range (k+1,0,-1):
#             print(j,end="")
#     for l in range (2,k+2):
#            print(l,end='')
#     print('')

#9
# a = int (input ( 'enter the number :'))

# for k in range (a):
    # for i in range (0,a-k):
            # print(" ",end="")
    # for j in range (k+1,0,-1):
            # print(j,end="")
    # for l in range (2,k+2):
        #    print(l,end='')
    # print('')
# for k in range (a,-1,-1):
    # for i in range (0,a-k):
            # print(" ",end="")
    # for j in range (k+1,0,-1):
            # print(j,end="")
    # for l in range (2,k+2):
        #    print(l,end='')
    # print('')
# 
##10
# a = int (input ( 'enter the number :'))
# 
# for k in range (a):
    # for i in range (0,a-k):
            # print(" ",end="")
    # for j in range (k+1,0,-1):
            # print('*',end="")
    # for l in range (2,k+2):
        #    print('*',end='')
    # print('')
# for k in range (a,-1,-1):
    # for i in range (0,a-k):
            # print(" ",end="")
    # for j in range (k+1,0,-1):
            # print('*',end="")
    # for l in range (2,k+2):
        #    print('*',end='')
    # print('')


# ##11
# a = int (input ( 'enter the number :'))

# for k in range (a):
#     for i in range (0,a-k):
#             print(" ",end="")
#     for j in range (k+1,0,-1):
#         if j==k+1 :
#             print('*',end="")
#         else:
#             print(' ',end='')
#     for l in range (2,k+2):
#             if l==k+1 :
#                 print('*',end="")
#             else:
#                 print(' ',end='')
#     print('')
# for k in range (a,-1,-1):
#     for i in range (0,a-k):
#             print(" ",end="")
#     for j in range (k+1,0,-1):
#         if j==k+1:
#             print('*',end="")
#         else: 
#             print(' ',end="")
#     for l in range (2,k+2):
#         if l==k+1:
#             print('*',end="")
#         else: 
#             print(' ',end="")
#     print('')

##12

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


# a=int (input ( 'enter the number :'))
# for k in range (a):
#     for i in range (0,a-k):
#             print(" ",end="")
#     for j in range (k+1,0,-1):
#             print(j,end="")
#     for l in range (2,k+2):
#            print(l,end='')
#     print('')



# # #13
# # r=[7,6,5,4,8,2,1]
# # k=13
# # for i in range (0,len(r)):
# #    for j in range (0,i):
# #         if  r[i]+r[j]==k:
# #             print(r[i],'+',r[j],'=',k)
      



# ##14

# a = int (input ( 'enter the number(2-9) :'))
# for k in range (a):
#     for i in range (a-k,0,-1):
#             print(i,end="")
#     for j in range (k):
#             print(" ",end="")
#     for l in range (k,0,-1):
#            print(" ",end='')
#     for i in range (1,a-k+1):
#         print(i,end="")
#     print('')
# for k in range (a-1,-1,-1):
#     for i in range (a-k,0,-1):
#             print(i,end="")
#     for j in range (k):
#             print(" ",end="")
#     for l in range (k,0,-1):
#            print(" ",end='')
#     for i in range (1,a-k+1):
#         print(i,end="")
#     print('')

##15
# a=int (input ( 'enter the number :'))
# for k in range (a):
#     for i in range (0,a-k):
#             print(" ",end="")
#     for j in range (k+1,0,-1):
#             print(j,end="")
#     for l in range (2,k+2):
#            print(l,end='')
#     print('')