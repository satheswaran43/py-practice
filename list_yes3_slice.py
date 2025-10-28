# # 1:extract last 3 ellements

# int=['paris','london','tokyo','new york','delhi']
# print(int[2:len(int)])

# # 2:print index 2 till the last element

# lst5=[0,1,2,3,4,5]
# print(lst5[2:len(lst5)])

# # 3:print every third element

# ls3t=[0,1,2,3,4,5,6,7,8,9]
# print(ls3t[2:len(ls3t):3])

# # 4:remove middle value from odd list

# ls2t=[1,2,3,4,5]
# middle_index=len(ls2t)//2
# print(ls2t[:middle_index]+ls2t[middle_index+1:])

# # 5:remove middle values from even list

# l2st=[1,2,3,4,5,6]
# middle_inde= (len(l2st)-1)//2
# middle_inde2=len(l2st)//2
# k=(l2st[:middle_inde ])+l2st[middle_inde2+1:]
# print(k)

# 6:palindrome using slicing

# st=[1,2,3,2,1]
# if st==st[::-1]:
#     print('true')
# else:
#     print('False')

# # 7:REVERSE THE SECOND HALF OF LIST

# ls4t=[10,20,30,40,50,60]
# st=len(ls4t)//2
# st2=(ls4t[:len(ls4t)//2]+ls4t[st:][::-1])
# print(st2)

# # 8:print all except last 2

# input=[1,2,3,4,5]
# b=(input[:len(input)-2])
# print(b)


# # 9:pint even index of the list

# st4=['a','b','c','d','e','f']
# l=st4[:len(st4):2]
# print(l)

# # 10:slice using variable start and end
# # task:Take input for start and end,and slice the list [100,200,300,400,500]

# i=[100,200,300,400,500]
# start=int(input('enter the number '))
# end=int(input('enter the value'))
# print(i[start:end])


