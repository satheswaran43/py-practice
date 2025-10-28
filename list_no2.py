sample_list=[10,30,50]
middle_index=(len(sample_list)//2)
k=sample_list[middle_index]

if k>sample_list[0] and k>sample_list[2]:
    print('yes')

elif k<=sample_list[0] and k<=sample_list[2]:
    print('not greater')