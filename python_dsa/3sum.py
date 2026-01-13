nums = [-1,0,1,2,-1,-4]

nums.sort()
ans = []

n = len(nums)

#[ 0,  1,  2,  3,4, 5]
# -4, -1, -1, 0, 1, 2,
#  i   j            k
for i in range(n): 
    if i > 0  and nums[i] == nums[i-1]:
        continue
    j = i+1
    k = n-1
    while j < k:
        sum_3 = nums[i]+ nums[j] + nums[k]
        if sum_3 == 0:
            ans.append([nums[i], nums[j], nums[k]])
            
            j += 1
            k -= 1
            
            while j < k and nums[j] == nums[j-1]:
                j += 1
            while j < k and nums[k] == nums[k+1]:
                k -= 1
            
        elif sum_3 > 0:
            k -= 1
        else:
            j += 1
    
print(ans)