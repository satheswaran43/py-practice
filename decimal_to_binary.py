##my code

a=24
i=0
lis=[]
while i<a:

    k=(a%2)
    lis.append(k)
    lis.sort(reverse=True)
    a//=2
print((int(str(lis).replace(", ","").replace("[","").replace("]",""))))




##akka code
# a=int(input ('enter the val'))
# s=""
# while a>0:
#     k=(a%2)
#     s=str(k)+s
#     a//=2
# print(s)
