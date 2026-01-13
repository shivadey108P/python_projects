def div(a, b):
    if b > 0:
        return a//b
    else:
        raise ZeroDivisionError
    
try:
    result = div(10,0)
except ZeroDivisionError as msg:
    print(f"Cannot divide by zero: {msg}")
else:
    print(result)

print("End of program")