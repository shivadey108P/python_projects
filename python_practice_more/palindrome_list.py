list1 = [5, 4, 3, 3, 4, 5]

# reverse = list(reversed(list1))
reverse = list1[::-1]


if list1 == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
