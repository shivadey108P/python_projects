def outer_func():
    print("I'm outer func")
    
    def inner_func():
        print("I'm inner func")
        
    return inner_func

inner_func = outer_func()
inner_func()