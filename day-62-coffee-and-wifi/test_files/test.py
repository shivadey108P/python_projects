import csv
from pprint import pprint

with open('./day-62-coffee-and-wifi/static/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            
# pprint(list_of_rows)

# print(list_of_rows[0])

# for row in list_of_rows[1:]:
#     for element in row:
#         if element.startswith('http'):
#             print('Map Link')
#         else:
#             print(element)
            
for row in list_of_rows[1:]:
    for index, element in enumerate(row):
        if index==1 and element.startswith('http'):
            print('Map Link')
        else:
            print(element)
    
# for element in list_of_rows[0]:
#     print(element)