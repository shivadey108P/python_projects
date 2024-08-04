try:
    file = open('./day-30/a_file.txt')
    a_dict = {'key': 'value'}
    print(a_dict['key'])
except FileNotFoundError as error:
    print(f"Didn't find file: {error.filename}, I will create one for you!")
    with open('./day-30/a_file.txt', mode='w') as file:
        file.write('Written something as exception was invoked!')
except KeyError as error:
    print(f"The key: {error}, doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('File was closed.')
