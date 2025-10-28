
##1 add five  in every index of the list
# p = [1, 2, 3, 4, 5]
# def i(p,l):
#  for i in range(len(p)):
#      p[i]+=l
#  print(p)
# i(p,5)


##2 double the odd number and half the even number 
# p = [2, 3, 4, 5]
# def i(p,l):
#  for i in range(len(p)):
#      if p[i]%2!=0:
#       p[i]*=l
#      elif p[i]%2==0:
#        p[i]//=l
#  print(p)
# i(p,2)

##3 find the given number is in the list 

p=[2,3,4,5,6]
k=int (input ('enter the number '))
def l(p,k):
    if k in p:
        print('the value found ')
    else:
        print('the value is not found ')
l(p,k)    