from typing import List

word_example_indiviual_words: List[str] = []


def get_word_example(response_word_example_block: List[str]) -> List[str]:
    for j in response_word_example_block:
        word_example_indiviual_words.append(j.text)

    # Save it in the format: word - meaning - "example"
    word_example_indiviual_words.insert(0, "\"")
    word_example_indiviual_words.append("\"")

    return ''.join(word_example_indiviual_words)
