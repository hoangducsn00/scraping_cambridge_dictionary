from typing import List



def get_word_meaning(response_word_meaning_block: List[str]) -> List[str]:
    word_meaning_indiviual_words: List[str] = []
    for i in response_word_meaning_block:
        word_meaning_indiviual_words.append(i.text)
    result = ''.join(word_meaning_indiviual_words)
    result = result.replace("\n", "").replace('"', '').strip()
    return result
