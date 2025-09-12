import random as rd

# rd.seed(10)

# for i in range(5):
#     print(rd.randrange(1,50))

lst = [1, 2, 3, 4, 5, 6]
rd.shuffle(lst)
print(f"Shuffled list: {lst}")
