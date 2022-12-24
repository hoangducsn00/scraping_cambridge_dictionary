from typing import List
from bs4 import BeautifulSoup
from requests import get
from functions.validate_input import isValidWord

word = input('Enter the word you\'re looking for:\n')

if isValidWord(word):
    url = f'https://dictionary.cambridge.org/dictionary/english/{word.strip()}'

    # Fake Google Chrome
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response_word = get(url, headers=headers)

    # Meaning of the searched word
    word_meaning: str = ''

    # An example of the searched word in a sentence
    word_example: str = ''

    # with open('data.html', mode='r', encoding="utf-8") as html_file:
    # html_file.write(response_word.text)
    soup = BeautifulSoup(response_word.text, "html5lib")

    response_word_meaning_block = soup.find(
        'div', {'class': 'def ddef_d db'}).children

    response_word_example = soup.find(
        'div', {'class': 'examp dexamp'}).children

    word_meaning_indiviual_words: List[str] = []
    word_example_indiviual_words: List[str] = []

    for i in response_word_meaning_block:
        word_meaning_indiviual_words.append(i.text)

    for j in response_word_example:
        word_example_indiviual_words.append(j.text)

    # Remove the last colon
    word_meaning_indiviual_words.pop()

    # Save it in the format: word - meaning - "example"
    word_example_indiviual_words.insert(0, "\"")
    word_example_indiviual_words.append("\"")

    word_meaning = f"{word} - " + ''.join(
        word_meaning_indiviual_words) + ' - ' + ''.join(word_example_indiviual_words)

    with open('words.txt', mode='a', encoding="utf-8") as my_vocab_list:
        my_vocab_list.write('\n')
        my_vocab_list.write('\n')
        my_vocab_list.write(word_meaning)

        print(f'{word} was successfully added to {my_vocab_list.name}')
else:
    print('Please provide a valid word.')
