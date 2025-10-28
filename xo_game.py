# ##first step:
xo=['-','-','-','-','-','-','-','-','-']

def game(gme):
 for i in range (len(gme)):
     print('|',gme[i],end="",)
     if (i+1)%3==0:
         print('|')


def rechange(ho):
 numbers=[]
 count=0
 for j in range (0,9):
    o=int(input('enter the number(1-9)'))
    if o in numbers :
     print('already entered number plese try again') 
    else:
     if count%2!=0:
      ho[o-1]='o'

     elif count%2==0 :
      ho[o-1]='x'  
    game(ho)

## finding the winner 
  ## if x is the winner the possibility
    if ho[0]=="x" and ho[1]=="x"and ho[2] =="x" or ho[3]=="x" and ho[4]=='x' and ho[5]=='x':
      print("X is the winner")
      break
   
    elif ho[6]=="x" and ho[7]=='x' and ho[8]=='x' or  ho[0]=="x" and ho[3]=='x' and ho[6]=='x':
    
      print("X is the winner")
      break
   
    elif ho[2]=="x" and ho[5]=='x' and ho[8]=='x'or ho[1]=="x" and ho[4]=='x' and ho[7]=='x':
     print("X is the winner")
     break
   
    elif ho[0]=="x" and ho[4]=='x' and ho[8]=='x' or   ho[2]=='x' and ho[4]=='x' and ho[6]=='x':
      print("X is the winner")
      break
    

  ## if o is the winner this is the possibility 
   
    if ho[0]=="o" and ho[1]=="o"and ho[2] =="o" or  ho[6]=="o" and ho[7]=='o' and ho[8]=='o':
      print("O is the winner")
      break
   
    elif ho[0]=="o" and ho[3]=='o' and ho[6]=='o'or ho[1]=="o" and ho[4]=='o' and ho[7]=='o':
      print("O is the winner")
      break
   
    elif ho[2]=="o" and ho[5]=='o' and ho[8]=='o' or ho[0]=="o" and ho[4]=='o' and ho[8]=='o':
      print("O is the winner")
      break
    
    elif ho[2]=='o' and ho[4]=='o' and ho[6]=='o'or ho[3]=="x" and ho[4]=='x' and ho[5]=='x':
      print("O is the winner")
      break
   
    if count == 9:
        print("It's a draw!")
        break

    count=count+1
    numbers.append(o)
rechange(xo)