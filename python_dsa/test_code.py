# str = "flow"

# print(len(str[0:100]))
# print(str[0:100])

all_res =[-3,-1,2]
target = 1

closest = min(all_res, key=lambda x: abs(x-target))
print(closest)