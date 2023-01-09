import sys
import logging
from typing import List
from bs4 import BeautifulSoup
from requests import get
from constants.request_config import URL, HEADERS
from functions.validate_input import isValidWord
from functions.format_word_meaning import get_word_meaning
from functions.format_word_example import get_word_example
from functions.save_word import save_word_to_file
import sys
import logging
from typing import List
from bs4 import BeautifulSoup
from requests import get
from tqdm import tqdm
import pandas as pd

logging.basicConfig(filename="log.txt", level=logging.ERROR)


if __name__ == '__main__':
    df = pd.read_csv('/Users/duc_lh/Documents/doan/py_word_processor/text_audio_urls.csv')
    words = df['word'].tolist()
    words_1 = words[1650:]
    for word in tqdm(words, total=len(words)):

        if isValidWord(word):
            response_word = get(URL + word, headers=HEADERS)

            # Meaning of the searched word
            # An example of the searched word in a sentence
            word_meaning = ''
            word_example = ''

            try:
                soup = BeautifulSoup(response_word.text, "lxml")

                response_word_meaning_block = soup.find(
                    'div', {'class': 'def ddef_d db'}).children

                response_word_example_block = soup.find(
                    'div', {'class': 'def-body ddef_b'}).children
            except Exception as err:
                logging.error(word)

            word_meaning = f"{word} - {get_word_meaning(response_word_meaning_block)} - {get_word_example(response_word_example_block)}"
            # print(word_meaning)
            save_word_to_file(word, word_meaning)
        else:
            save_word_to_file(str(word), "no page found in cambridge dictionary")
            # print(word_meaning)