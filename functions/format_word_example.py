from typing import List
import re



def get_word_example(response_word_example_block: List[str]) -> List[str]:
    word_example_indiviual_words: List[str] = []
    for j in response_word_example_block:
        text = j.text.replace("\n", "").replace('"', '').strip()
        result_2 = re.sub(' +', ' ', text)
        word_example_indiviual_words.append(result_2)
        word_example_indiviual_words.append("***")

    return ''.join(word_example_indiviual_words)
