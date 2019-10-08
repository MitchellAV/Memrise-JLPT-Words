import csv
import random

contents = []
kana = []
kanji = []
errors = []

jlptLow = 5
jlptHigh = 2

for w in range(5, jlptHigh - 1, -1):
    level = 'n'+str(w)

    line_limit = 1000

    with open(level + '.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            contents.append(line)


random.shuffle(contents)

currLine = 1
for line in contents:
    if (len(line[0]) == 0):
        kana.append(line)
    else:
        kanji.append(line)
        if (any(len(x) == 0 for x in line)):
            print(w,currLine,line[1],line[2])
            errors.append(line)
    currLine += 1

i = 0
file_num = 0
while (file_num < (len(kanji) / float(line_limit))):
    with open('grouped-levels/n'+str(jlptLow)+'-' +'n'+str(jlptHigh)+  '-kanji-' + str(file_num) + '.csv', 'w') as kanji_file:
        csv_writer = csv.writer(kanji_file, delimiter=',')

        for x in range(line_limit):
            if (i < len(kanji)):
                csv_writer.writerow(kanji[i])
                i += 1
            else:
                break
        file_num += 1
i = 0
file_num = 0
while (file_num < (len(kana) / float(line_limit))):
    with open('grouped-levels/n'+str(jlptLow)+'-' +'n'+str(jlptHigh)+ '-kana-' + str(file_num) + '.csv', 'w') as kana_file:
        csv_writer = csv.writer(kana_file, delimiter=',')

        for x in range(line_limit):
            if (i < len(kana)):
                csv_writer.writerow(kana[i])
                i += 1
            else:
                break
        file_num += 1
