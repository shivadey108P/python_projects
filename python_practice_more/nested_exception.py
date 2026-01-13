L = [10,20,30,40,50]

try:
    try:
        index = int(input("Enter the index you want to access: "))
    except ValueError as msg:
        print(msg)
    print(L[index])
except IndexError as msg:
    print(msg)
except NameError as msg:
    print(msg)


print("1" == 1)
print(L.index(20))