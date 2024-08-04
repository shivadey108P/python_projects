import pandas as pd
from random import randint
def selection_of_word():
    data = pd.read_csv('./day-31/flash-card-project-start/data/french_words.csv')
    words_data = data.to_dict(orient='records')
    dict_size = len(words_data)
    selection_of_word = randint(0, dict_size)
    french_word = words_data[selection_of_word]['French']
    english_word = words_data[selection_of_word]['English']
    return french_word, english_word

print(selection_of_word()[0])