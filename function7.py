
def hosqr (t):
    for i in range (0,t):
        for j in range (0,t):
            if i==0 or j==0 or i==t-1 or j==t-1 :
                print('*',end="")
            else :
                print(' ',end='')
        print('')



def hodim(a):
 for k in range (a):
     for i in range (0,a-k):
             print(" ",end="")
     for j in range (k+1,0,-1):
         if j==k+1 :
             print('*',end="")
         else:
             print(' ',end='')
     for l in range (2,k+2):
             if l==k+1 :
                 print('*',end="")
             else:
                 print(' ',end='')
     print('')
 for k in range (a,-1,-1):
     for i in range (0,a-k):
             print(" ",end="")
     for j in range (k+1,0,-1):
         if j==k+1:
             print('*',end="")
         else: 
             print(' ',end="")
     for l in range (2,k+2):
         if l==k+1:
             print('*',end="")
         else: 
             print(' ',end="")
     print('')


def hotri(a):

 
 for k in range (a):
     for i in range (0,a-k):
             print(" ",end="")
         
     for j in range (k+1,0,-1):
         if j==k+1 or k==a-1 :
             print('*',end="")
         else:
             print(' ',end='')
     for l in range (2,k+2):
             if l==k+1 or k ==a-1:
                 print('*',end="")
             else:
                 print(' ',end='')
 
     print('')



hotri(10)