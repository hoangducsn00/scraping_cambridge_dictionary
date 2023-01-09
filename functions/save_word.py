import os


def save_word_to_file(word: str = 'word', word_meaning: str = 'word meaning'):
    csv_line = word + ";" + str(word_meaning)
    with open('/Users/duc_lh/Documents/doan/py_word_processor/meaning_1.csv','a') as outfile:
      outfile.write(csv_line + "\n")
