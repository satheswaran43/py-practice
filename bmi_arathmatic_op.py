weight=float(input('enter weight(kg)'))
height=float(input('enter height(M)'))

BMI=weight/(height*height)

under_weight="tip:includemore calories in your meals such as nuts,dairy,and rice.Focus on strenght training and musclw gain exercises."
normal_weight='tip:maintain your balanced diet.Continue regular phusical acticities like walking youga or moderate cardeo.'
over_weight="tip:reduce sugar and fat intake. Include high-fiber foods and aim for 30 minuts of exercise like brisk walking or cycling daily."
obese="tip:Consult a dietitian. Adopt a calorie-deficit diet with fruits,vegetables,and grains.Engage in low-impact exercises like swimming or walking,gradually increasing intensity."

if BMI<18.5:
    print('Category:under weight')
    print( under_weight)

elif 18.5<=BMI<24.9:
    print('Category:normal weight')
    print(normal_weight)

elif 25<=BMI<29.9:
    print("Category:overweight")
    print(over_weight)

elif BMI>=30:
    print("Category:obese")
    print(obese)

