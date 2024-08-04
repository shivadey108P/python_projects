import pandas

data = pandas.read_csv("./day-30/NATO_Exec/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, please enter letters or alphabets')
        generate_phonetic()
    else:
        print(output_list)
        
generate_phonetic()
