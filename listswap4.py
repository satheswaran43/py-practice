# sample_list=[10,20,30,40,50]
# temp=0

# temp=sample_list[0]
# sample_list[0]=sample_list[4]
# sample_list[4]=temp

# print(sample_list)


sample_list=[10,20,30,40,50,80]
temp=0
print(len(sample_list))
temp=sample_list[0]
sample_list[0]=sample_list[len(sample_list)-1]
sample_list[len(sample_list)-1]=temp

print(sample_list)

