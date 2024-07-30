# # with open('./day-25\\weather_data.csv', mode='r') as file:
# #     data = file.readlines()
    
# # for row in data:
# #     print(row.strip())

# # import csv

# # with open('./day-25\\weather_data.csv', mode='r') as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
            
# # print(temperatures)

# import pandas as pd

# data = pd.read_csv('./day-25\\weather_data.csv')
# # temp_list = data['temp'].to_list()
# # average_temp = data['temp'].mean()
# # print(average_temp)

# # # no_of_data = len(temp_list)
# # # sum_of_temp = sum(temp_list)
# # # print(sum_of_temp/no_of_data)

# # max_temp = data['temp'].max()
# # print(max_temp)

# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp[0]
# monday_temp_F = (monday_temp * 9/5) + 32
# print(monday_temp_F)


import pandas as pd

squirrel_data = pd.read_csv('./day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

print(len(squirrel_data['Primary Fur Color'].values))

# Get unique values from 'Primary Fur Color' column and drop NaN values
color_s = squirrel_data['Primary Fur Color'].dropna().unique().tolist()

print(color_s)
count_s = []
# print(len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black']))
for color in color_s:
    count_s.append(len(squirrel_data[squirrel_data['Primary Fur Color'] == color]))

print(count_s)

data_dict  = {
    'Fur Color': color_s,
    'Count': count_s
}

df = pd.DataFrame(data_dict)
df.to_csv('./day-25/squirrel_count.csv')
