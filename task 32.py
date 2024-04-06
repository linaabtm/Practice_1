# Открываем файл и считываем данные
with open('freqs.txt', 'r') as file:
    data = file.read()
frequencies = [float(freq) for freq in data.replace(';', '\n').split('\n') if freq.strip() != '' and float(freq) < 11]
filtered_freqs_str = ' '.join(map(str, frequencies))
print(filtered_freqs_str)