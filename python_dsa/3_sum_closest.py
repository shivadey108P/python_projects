nums = [4,0,5,-5,3,3,0,-4,-5]
# nums = [-1,2,1,-4]
# nums = [0,0,0]
target = -2

def threeSumClosest(nums, target):
    
    nums.sort()
    n = len(nums)
    
    closest_sum = nums[0] + nums[1] + nums[2]
    
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = n - 1
        
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            
            if total == target:
                return total
            elif abs(total - target) < abs(closest_sum - target):
                closest_sum = total
            elif total>target:
                k -= 1
            else:
                j += 1
    return closest_sum


result = threeSumClosest(nums, target)
print(result)

