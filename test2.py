principal_amt=int(input("enter the amt"))
interst_rate_for_fd=int(input("enter the intrest"))
interst_rate_for_rd=int(input("enter your intrest2"))
compound_intrest=int(input('enter your ci'))
fixed_cashback_per_yer=int(input("enter cashback "))
time=1
time2=2
time3=3



simple_intrest=(principal_amt*interst_rate_for_fd*time)/100
fd_returns=principal_amt+simple_intrest
cashback=(principal_amt+fixed_cashback_per_yer*time)

simple_intrest2=(principal_amt*interst_rate_for_fd*time2)/100
fd_returns2=principal_amt+simple_intrest2
cashback2=(principal_amt+(fixed_cashback_per_yer*time2))

simple_intrest3=(principal_amt*interst_rate_for_fd*time3)/100
fd_returns3=principal_amt+simple_intrest3
cashback3=(principal_amt+(fixed_cashback_per_yer*time3))


p=simple_intrest/12
print(interst_rate_for_fd+interst_rate_for_rd)
# print(p)
# print(a)

# print("------------------------------------")
# print("|yer|policy1(fd)|policy4(hdfc) ")
# print("---------------------------------------------")
# print(time,"|",fd_returns,"|",cashback)
# print(time2,"|",fd_returns2,"|",cashback2)
# print(time3,"|",fd_returns3,"|",cashback3)

