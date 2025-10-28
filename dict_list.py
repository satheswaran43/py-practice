lis=[
    {"product":"Hp laptop","quantity":1,"price":25000,"category":'electronic device',"sno":1},
    {"product":"vivo mobile","quantity":1,"price":20000,"category":'electronic device',"sno":2},
    {"product":"black board","quantity":1,"price":5000,"category":'"educational tool',"sno":3},
    {"product":"chiar","quantity":10,"price":8000,"category":'furneature',"sno":4},
    {"product":"water fileter","quantity":2,"price":40000,"category":'water treatment',"sno":5},
       {"product":"Hp laptop","quantity":1,"price":25000,"category":'electronic device',"sno":6},
    {"product":"mobile","quantity":1,"price":20000,"category":'electronic device',"sno":7},
    {"product":" board","quantity":1,"price":5000,"category":'"educational tool',"sno":8},
    {"product":"table","quantity":10,"price":8000,"category":'furneature',"sno":9},
    {"product":"air fileter","quantity":2,"price":90000,"category":'water treatment',"sno":10},
]
lis.append({'product':'bag','quantity':5,'price':3500,'category':'external uses'})

print('-'*76)
print(f'|{"sno":<5}|{"produce":<25}|{"quantity":<10}|{"price":<10}|{"category":<20}|')
print('-'*76)
j=1
for i in (lis):
    # if i["price"]>=10000:
        print(f"|{j:<5}|{i['product']:<25}|{i['quantity']:<10}|{i['price']:<10}|{i['category']:<20}|")
        j+=1
        print('-'*76)