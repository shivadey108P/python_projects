import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

word_list =pandas.read_csv('./day-26/NATO-alphabet-start/nato_phonetic_alphabet.csv')

word_dict = {row.letter: row.code for(index, row) in word_list.iterrows()}

    
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = (input('Enter your name: ')).upper()

code_list = [word_dict[word] for word in name]
print(code_list)