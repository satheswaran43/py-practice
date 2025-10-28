hemog=float(input('enter your level'))
gender=input('enter your gender')

if gender=='male':
    if hemog<=17.5 and hemog>13.5:
        print('normal level')
    elif hemog<=13.5 and hemog>10:
        print('mild anemia')
 

elif gender=='female':
    if hemog<=16 and hemog>12:
        print('normal')
    elif hemog<=12 and hemog>10:
        print('mild anemia')
      
    
if hemog>=8 and hemog<=10: 
        print('moerate anemia')
if hemog<8 and hemog>=1:
        print('severe anemia')
elif hemog>20 or hemog<1:
        print('invalid')
