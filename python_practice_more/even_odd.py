nums = [4, 8, 3, 5, 10, 7, 2, 9, 13, 6]

odd = [num for num in nums if num % 2 != 0]

even = [num for num in nums if num % 2 == 0]

# for num in nums:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

print(f"Odd nums: {odd}")
print(f"Even nums: {even}")
