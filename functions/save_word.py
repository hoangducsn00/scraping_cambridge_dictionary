import os


def save_word_to_file(word: str = 'word', word_meaning: str = 'word meaning'):
    with open('words.txt', mode='a', encoding="utf-8") as my_vocab_list:
        if os.path.getsize('words.txt') == 0:
            my_vocab_list.write(word_meaning)
            print(f'{word} was successfully added to {my_vocab_list.name}')
            return
        my_vocab_list.write('\n')
        my_vocab_list.write('\n')
        my_vocab_list.write(word_meaning)
        print(f'{word} was successfully added to {my_vocab_list.name}')
