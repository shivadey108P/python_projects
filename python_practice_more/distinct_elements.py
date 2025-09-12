list1 = [3,5,7,2,1,3,7,5,4,8,3]

res = []

for num in list1:
    if num not in res:
        res.append(num)
        
print(res)