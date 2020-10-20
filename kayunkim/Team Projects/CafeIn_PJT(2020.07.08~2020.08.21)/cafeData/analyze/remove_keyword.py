stop_words = []
with open('stopwords.txt', 'r', encoding='utf-8-sig') as f:
    while True:
        line = f.readline()
        if not line: break
        stop_words.append(line.replace('\n', ''))

keywords = []
with open('keywords.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break

        line = line.replace('\n', '').split(',')[2]
        if line not in stop_words:
            keywords.append(line)

with open('new.txt', 'w', encoding='utf-8') as f:
    for key in keywords:
        f.write(key + '\n')