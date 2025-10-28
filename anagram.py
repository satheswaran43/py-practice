# v='tan'
# o='nat'
# l=[i for i in v]
# l1=[i for i in o]
# l.sort()
# l1.sort()
# print(l)
# print(l1)
# if l==l1:
#     print('yes')
# else:print('noop')

p=['tan','nat','hop','poh','noop']
y=[]

for i in range (len(p)):
    # print(p[i])
    l=[j for j in p[i]]
    l.sort()
    status =False
    y.append(l)
print(y)
    # for k in range (len(y)):
    #     for d in range (k):
    #         if y[k]==y[d]:

    #            print('yes')
    #         else :
    #             print('noo')