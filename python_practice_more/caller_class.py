import calendar as cal

# print(list(cal.day_name))
class Day:
    def __init__(self):
        self.days = dict(enumerate(cal.day_name, start=1))
        
    def __call__(self, day_num):
        return self.days.get(day_num, f"Invalid Day number: {day_num}")
    
d = Day()
print(d(7))
print(d(0))