import json
from collections import Counter

log_data = []
with open('skillbox_json_messages.log', 'r') as file:
    for line in file:
        log_data.append(json.loads(line))

# Задача 1: Сколько было сообщений каждого уровня за сутки
level_counts = Counter(entry['level'] for entry in log_data)
print(f'Количество сообщений каждого уровня: {level_counts}')

# Задача 2: В какой час было больше всего логов
hour_counts = Counter(entry['time'].split(':')[0] for entry in log_data)
most_common_hour = hour_counts.most_common(1)[0][0]
print(f'Час с наибольшим количеством логов: {most_common_hour}')

# Задача 3: Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00
critical_logs_count = sum(1 for entry in log_data if entry['level'] == 'CRITICAL' and '05:00:00' <= entry['time'] <= '05:20:00')
print(f'Количество логов уровня CRITICAL в период с 05:00:00 по 05:20:00: {critical_logs_count}')

# Задача 4: Сколько сообщений содержат слово "dog"
word_counts = Counter(entry['message'] for entry in log_data if 'dog' in entry['message'])
dog_messages_count = sum(word_counts.values())
print(f'Количество сообщений, содержащих слово "dog": {dog_messages_count}')

# Задача 5: Какое слово чаще всего встречалось в сообщениях уровня WARNING
warning_messages = [entry['message'] for entry in log_data if entry['level'] == 'WARNING']
warning_word_counts = Counter(word for message in warning_messages for word in message.split())
most_common_warning_word = warning_word_counts.most_common(1)[0][0]
print(f'Слово, которое чаще всего встречалось в сообщениях уровня WARNING: {most_common_warning_word}')
