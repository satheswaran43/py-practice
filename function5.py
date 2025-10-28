# status=False
# def numbers(lst,k):
#     for i in range (len(lst)):
#      if lst[i]==k:
#         status=True
#     if status:
#      print('yes')
#     else:
#         print('noop')

# numbers([1,2,3,5,7,8,10],10)


# def num(lis):
#     value=[]
#     coutn=[]
#     for i in lis:
#      if i not in value:
#         value.append(i)
#         coutn.append(lis.count(i))
#     max1 = max(coutn)
#     max_2= value[coutn.index(max1)]
#     print(max1)
    
# num([1,2,3,5,5,7,8,10])




def num (lis,l):
    print(lis.count(l))
num([1,2,3,5,5,7,8,10],5)
