lst = [1, 2, 3, 4, 5, 6]
print(f"Current list: {lst}")
k = int(input("How may times the  rotation is required for the above list?: 1"))
rotated = lst[k:] + lst[:k]
print(rotated)
