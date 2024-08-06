def factorial(n):
    if n == 1:
        return n
    n *= n
    n -= 1
    factorial(n)
    
print(factorial(5))