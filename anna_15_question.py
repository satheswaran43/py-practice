# ##1.sum of lists:
# marks=[85,90,78,92]
# print(sum(marks))


# ##2.find the highest mark:
# marks2=[85,90,78,92]
# print(max(marks2))

# ##3.reverse the student list:
# student=['john','alice','bob']
# print(student[::-1])

# ##4.check if students exists

# student=['john','alice','bob']
# check='alice'
# for i in student:
#     if check==i:
#         print(i)

# ##5.remove duplicate names

# student=['john','alice','bob','alice']
# l=(set(student))
# p=list(l)
# print(p)

# ##6.count name occurrences:
# student=['john','alice','john','bob','john','alice']
# find='john'
# print(student.count(find))

# ##7.find student index:
# student=['john','alice','bob','alice']
# name='bob'
# for i in range (len(student)):
#     if name ==student[i]:
#         print(i)

# ##8.merge two class lists without duplicates:
# student=['john','alice']
# clas=['bob','alice']
# p=set(clas+student)
# l=list(p)
# print(l)

# ##9.filter passing students:
# marks3=[45,78,89,32,60]
# a=[]
# for i in marks3:
#     if i>=50:
#      a.append(i)
# print(a)   

# ##10.find second highest mark:
# marks5=[85,90,78,92]
# marks5.sort()
# print(marks5[-2])


# ##11.rotate student roll number:
# rolls=[1,2,3,4,5]
# k=2
# l=(rolls[:-k])
# o=rolls[-k:]
# print(o+l)

# ##12.flatten nested student groups:
# groups =[['john','slice'],['bob',['sara']]]
# c=[]
# a= groups[0]
# b=groups [1][0]
# c.append(b)
# d=groups [1][1]
# print(a+c+d)


# # ##13.convert student names to string:
# student3=['john','alice','bob']
# p=','.join(student3)    
# print(p)
# # s="vel"
# # s1="eswaran"
# # name =s+","+s1

# ##14.find common students in two class:
# classa=['john','alice','bob']
# classb=['john','slice','bob']
# print(list(set(classa) & set(classb)))

##15.split a list into two groups:

students=['john','alice','bob','sara','tom']
p=[]
o=[]
k=[]
p.append(students[0])
p.append(students[1])
o.append(students[2])
o.append(students[3])
k.append(students[4])
print([p,o,k])