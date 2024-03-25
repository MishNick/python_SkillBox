import re


def load_word_list(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split('\n')
    return set(map(str.lower, words))


word_list = load_word_list('/usr/share/dict/words')


def is_strong_password(password):
    password = password.lower()

    words = re.findall(r'\b\w+\b', password)

    for word in words:
        if word in word_list:
            return False
    return True


# Пример использования
password = 'MyPassword123'
if is_strong_password(password):
    print(f'Пароль "{password}" является хорошим')
else:
    print(f'Пароль "{password}" не является хорошим')
