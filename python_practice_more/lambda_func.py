l1 = [1,2,3,4,5,6,7,8,9,10]

f = filter(lambda x: x%3 == 0, l1)

print(list(f))

m = list(map(lambda x: -x**2, l1))

print(m)

k = lambda x: x if x%2 == 0 else -x*2

odd = list(map(k, l1))

print(odd)

l2 = [[4,2,"Six"], [1,4,"Five"], [2,2,"Four"], [1,1,1,"Three"], [1,1,5, "Seven"]]

l3 = sorted(l2, key= lambda x: sum(val for val in x if isinstance(val, int)))

print(l3)

list1 = [1,2,3,4, "Five"]
s = sum(x for x in list1 if isinstance(x, int))
print(s)