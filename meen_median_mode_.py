# # median
# r=[1,2,3,4,5]
# print(len(r))
# middle_index=(len(r)//2)
# k=r[middle_index]
# print('median=',k)

# #mean
# r2=[1,2,3,4,9,8]
# sum=0

# for num in r2:
#  sum+=num
# mean= sum/len(r2)
# print('mean=',mean)

# ##mode

# lis=[1,2,3,4,4,5,4]
# val=[]
# c=[]
# for num in lis:
#      if num not in val:
#         val.append(num)
#         c.append(lis.count(num))
# max = max(c)
# max_2= val[c.index(max)]
# print(val)
# print(c)
# print(max_2)


### mode
# dic={}
# lis=[2,2,3,4,5,6,4,3,2]
# for num in lis:
#     if num not in dic:
#         dic[num]=lis.count(num)
# print(max(dic, key=dic.get))
# print(dic.get(4)) 

# print(max(dic.values()))

