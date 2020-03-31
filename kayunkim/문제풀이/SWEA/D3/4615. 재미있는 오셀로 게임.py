sam = {}
for i in enumerate(range(4)):
    sam[i[0]] = i[1]

print(sum(sam.values()))