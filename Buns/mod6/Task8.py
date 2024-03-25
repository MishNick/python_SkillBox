import re


def my_t9(sequence):
    digit_to_letter = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    with open('/usr/share/dict/words', 'r') as f:
        word_list = f.read().splitlines()

    combinations = ['']
    for digit in sequence:
        letters = digit_to_letter.get(digit)
        combinations = [prefix + letter for prefix in combinations for letter in letters]

    valid_words = []
    for combination in combinations:
        if re.match(r'\b' + combination + r'\b', ' '.join(word_list), re.IGNORECASE):
            valid_words.append(combination)

    return valid_words
