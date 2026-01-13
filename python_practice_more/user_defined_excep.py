class NegativeDimensionError(Exception):
    def __init__(self):
        self.msg = "Negative dimensions were given!"
        
    def __str__(self):
        return self.msg
    
def area(length, breadth):
    if length>0 and breadth>0:
        return length*breadth
    else:
        raise NegativeDimensionError()
    
print(area(5,10))