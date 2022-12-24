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

logging.basicConfig(filename="log.txt", level=logging.ERROR)


if __name__ == '__main__':
    word = input('Enter the word you\'re looking for:\n')

    if isValidWord(word):
        response_word = get(URL + word, headers=HEADERS)

        # Meaning of the searched word
        # An example of the searched word in a sentence
        word_meaning = ''
        word_example = ''

        try:
            soup = BeautifulSoup(response_word.text, "html5lib")

            response_word_meaning_block = soup.find(
                'div', {'class': 'def ddef_d db'}).children

            response_word_example_block = soup.find(
                'div', {'class': 'examp dexamp'}).children
        except Exception as err:
            logging.error(
                f'\n\nSomething went wrong, please check the api.\n\n')
            print('Something went wrong.')
            sys.exit(1)

        word_meaning = f"{word} - {get_word_meaning(response_word_meaning_block)} - {get_word_example(response_word_example_block)}"

        save_word_to_file(word, word_meaning)
    else:
        print('Please provide a valid word. (Avoid using numbers or special characters)')
