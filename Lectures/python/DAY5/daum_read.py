import csv

with open('daum_rank.csv', 'r', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['rank'], row['ranker'])