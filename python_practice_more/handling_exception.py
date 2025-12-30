L = [10,20,30,40,50]

try:
    index = int('abc')
    print(L[index])
except (IndexError, TypeError, ValueError) as msg:
    print(msg)
    
print("End of the program")