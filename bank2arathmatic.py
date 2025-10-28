annual_incom=int(input('enter incom value'))
if annual_incom<250000:
    print("no tax")

elif 250000>annual_incom<=500000:
    print(((annual_incom-250000)*5)/100)

elif 500000>annual_incom<=1000000:
     print(((annual_incom-250000)*20)/100)

elif annual_incom>1000000:
    print(((annual_incom-250000)*30)/100)
