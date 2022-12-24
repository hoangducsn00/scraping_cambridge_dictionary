from typing import List

word_meaning_indiviual_words: List[str] = []


def get_word_meaning(response_word_meaning_block: List[str]) -> List[str]:
    for i in response_word_meaning_block:
        word_meaning_indiviual_words.append(i.text)

    # Remove the last colon
    word_meaning_indiviual_words.pop()

    return ''.join(word_meaning_indiviual_words)
