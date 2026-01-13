nums = [2, 11, 15, 7]
target = 9

hash = {}

for n in range(len(nums)):
    req_val = hash.get((target - nums[n]))
    if req_val is not None:
        print([req_val, n])
    else:
        hash[nums[n]] = n

print(hash)
