def fun():
    try:
        val = int('256')
        return val
    except ValueError as e:
        raise e
    finally:
        print("End of the function")

      
print(fun())