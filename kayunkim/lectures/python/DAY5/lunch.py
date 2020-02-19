import csv

lunch = {
    '양자강' : '02-557-4211',
    '세븐브릭스': '02-488-4744',
    '멀캠20층': '02-0000-2424'
}

with open('lunch.csv', 'w', encoding='utf-8', newline ='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for item, number in lunch.items():
        csv_writer.writerow([item,number])


# csvfile = open('lunch.csv', 'w', encoding='utf-8', newline='')  # newline='' 추가해서 간격 없애기
# csv_writer = csv.writer(csvfile)

# for item, number in lunch.items():
#     csv_writer.writerow([item,number])

# csvfile.close()