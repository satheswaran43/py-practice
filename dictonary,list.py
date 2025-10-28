# fb=[ 
#         {
 
#             "name":"satheswaran",
#             "nicname":"dudu",
#             'mobile number':'9442083089',
#             "DOB":'27/10/2007',
#             "password":'6363',
#             'recovery email':'sathes@gmail',
#             'gender':'male'
# },

# {
#     "name":"kannan",
#     "nicname":"kanna",
#     'mobile number':'9442083089',
#     "DOB":'27/10/2007',
#     "password":'6363',
#     'recovery email':'sathes@gmail',
#     'gender':'male'
# }
# ]
# print(fb[0]['name'])
# fb={
#     "name":"kannan",
#     "nicname":"kanna",
#     'mobile number':'9442083089',
#     "DOB":'27/10/2007',
#     "password":'6363',
#     'recovery email':'sathes@gmail',
#     'gender':'male'
# }
dic={}
lis=[2,2,3,4,5,6,4,3,2]
for num in lis:
    if num not in dic:
        dic[num]=lis.count(num)
print(max(dic, key=dic.get))
print(dic.get(4))

# print(max(dic.values()))
