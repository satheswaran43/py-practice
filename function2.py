# #1
# r=int(input("entr the number "))

# def square (r):
#     i=1
#     v=r**2
#     while i<=v:
#         print("*",end="")
#         if i%r==0:
#             print('')
#         i+=1
# square(r)

# #2

# # a = int (input ( 'enter the number :'))
# # def triangle(a):
# #     for k in range (a,-1,-1):
# #         for i in range (0,a-k):
# #                 print(" ",end="")
# #         for j in range (k+1,0,-1):
# #                 print('*',end="")
# #         for l in range (2,k+2):
# #                print('*',end='')
# #         print('')
# # triangle(a)

# # #3
# # a = int (input ( 'enter the number :'))
# # def triangle(a):
# #     for k in range (a,):
# #         for i in range (1,a-k):
# #                 print(" ",end="")
# #         for j in range (k+1,0,-1):
# #                 print('*',end="")
# #         for l in range (2,k+2):
# #                print('*',end='')
# #         print('')
# # triangle(a)

# # #4

# # a = int (input ( 'enter the number :'))
# # def dim(a):
# #     for k in range (a):
# #         for i in range (0,a-k):
# #                 print(" ",end="")
# #         for j in range (k+1,0,-1):
# #                 print('*',end="")
# #         for l in range (2,k+2):
# #                print('*',end='')
# #         print('')
# #     for k in range (a,-1,-1):
# #         for i in range (0,a-k):
# #                 print(" ",end="")
# #         for j in range (k+1,0,-1):
# #                 print('*',end="")
# #         for l in range (2,k+2):
# #                print('*',end='')
# #         print('')
# # dim(a)






# a = int (input ( 'enter the number(2-9) :'))
# def outdim(a):
       
#  for k in range (a):
#      for i in range (a-k,0,-1):
#              print(i,end="")
#      for j in range (k):
#              print(" ",end="")
#      for l in range (k,0,-1):
#             print(" ",end='')
#      for i in range (1,a-k+1):
#          print(i,end="")
#      print('')
#  for k in range (a-1,-1,-1):
#      for i in range (a-k,0,-1):
#              print(i,end="")
#      for j in range (k):
#              print(" ",end="")
#      for l in range (k,0,-1):
#             print(" ",end='')
#      for i in range (1,a-k+1):
#          print(i,end="")
#      print('')
# outdim(a)
