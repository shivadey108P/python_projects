nums = [-1,0,1,2,-1,-4]

# -4, 0, 1, 2, -1, -1

n = len(nums)
j = n-1

res = []

for i in range(n):
    if nums[j] <= nums[i]:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    elif nums[j] >= nums[i]:
        j -= 1

print(nums)
        