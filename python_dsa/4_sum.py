# nums = [1,0,-1,0,-2,2]
nums = [-1,0,-5,-2,-2,-4,0,1,-2]
# target = 0
target = -9

def fourSum(nums, target: int):
    """
    Finds all unique quadruplets that sum to the target.

    :param nums: List of integers
    :param target: Target sum
    :return: List of quadruplets
    """
    nums.sort()
    n = len(nums)
    result = []

    # -2, -1, 0, 0, 1, 2
    #  i,  j, l,       k

    for first in range(n - 3):
        if first> 0 and nums[first] == nums[first-1]:
            continue
        for second in range(first+1, n-2):
            if second > first+1 and nums[second] == nums[second-1]:
                continue
            left = second+1
            right = n-1

            while left<right:
                total = nums[first] + nums[second] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[first], nums[second], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
                elif total > target:
                    right -= 1
                else:
                    left += 1
    return result


print(fourSum(nums, target))