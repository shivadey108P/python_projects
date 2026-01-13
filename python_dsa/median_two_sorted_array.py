nums1 = [1,3]
nums2 = [2]

final = nums1 + (nums2)
final.sort()

n = len(final)

if n%2 == 0:
    median = (final[n//2 -1]+ final[n//2])/2
    print(median)
else:
    print(final[n//2])
