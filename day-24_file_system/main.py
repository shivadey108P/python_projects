# with open('day-24_file_system\\my_file.txt', mode= 'a') as file:
#     file.write('\nI have added a new line to the file.')


with open('day-24_file_system\\my_file.txt') as file:
    contents = int(file.read())
    print(contents)
    print(type(contents))
    
    
# with open('day-24_file_system\\new_file.txt', mode= 'w') as file:
#     file.write('I have created a new file.')

