import json
import csv

jsonData = {}
data = []
words = []
allKana = []
fileName = 'jlpt-n1'

with open(fileName + ".json","r", encoding="utf-8") as f:
    jsonData = json.load(f)
    for x in jsonData["data"]:
        data.append(x)

print(len(data))

for index, entry in enumerate(data, 0):
    
    # if (index != 0):
    #     try:
    #         if entry['japanese'][0]['word'] not in allKana:
    #             allKana.append(entry['japanese'][0]['word'])
    #         else:
    #             print(index, entry['japanese'][0]['word'])
    #             continue
    #     except KeyError:
    #         pass    


    obj = {
        'kanji': [],
        'kana': [],
        'english': '',
        'parts_of_speech': '',
        'is_common': entry['is_common'],
        'jlpt': entry['jlpt'],
        'kana_only': None,
        'csv': [],
        'check': []
    }
    for x in entry['japanese']:

        try:
            obj['kanji'].append(x['word'])
        except KeyError:
            obj['kanji'].append('')
        
        # try:
        obj['kana'].append(x['reading'])
        
        # except KeyError:
        #     obj['kana'].append('')

    english = ''
    parts_of_speech = ''
    lastkana = ''
    defCount = 0
    defLimit = 144

    pos = []

    for i, x in enumerate(entry['senses'], 0):
        kanaOnly = any('kana' in s for s in x['tags'])
        obj['kana_only'] = kanaOnly
        wikiCheck = x['parts_of_speech']
        if len(wikiCheck) != 0:  
            if 'wikipedia' in wikiCheck[0].lower():
                continue
        # if i < 4:
        for j, val in enumerate(x['english_definitions'], 0):
            defCount += len(val)    
            if (i == 0 and j == 0):
                english += val
            elif j < 4 and defCount < defLimit:    
                english += '; ' + val  
        for j, val in enumerate(x['parts_of_speech'], 0):
            
            if (i == 0 and j == 0):
                parts_of_speech += val
                pos.append(val)
            elif(val not in pos):
                parts_of_speech += '; ' + val 
                pos.append(val)
    
    obj['parts_of_speech'] += parts_of_speech    
    obj['english'] += english
    obj['check'] = f"\"{obj['kana'][0]}\",\"{obj['english']}\",\"{obj['kanji'][0]}\",\"{obj['parts_of_speech']}\""
    obj['csv'] = [obj['kana'][0], obj['english'], obj['kanji'][0], obj['parts_of_speech']]
    
    if (index == 0):
        words.append(obj)
    else:
        for el in words:
            if(obj['check'] == el['check']):
                break
        else:
            words.append(obj)

kanjiList = []
kanaList = []

for word in words:  
    if word['kana_only'] or word['kanji'][0] == '':
        kanaList.append(word['csv'])
    else:
        kanjiList.append(word['csv']) 
    

line_limit = 250
print(len(kanaList)+len(kanjiList), len(allKana))

i = 0
file_num = 0
while (file_num < (len(kanjiList) / float(line_limit))):
    with open('jlpt/' + fileName + '-kanji-' + str(file_num) + '.csv', 'w', encoding="utf-8", newline='') as f:
        csv_writer = csv.writer(f, delimiter=',')
        for x in range(line_limit):
            if (i < len(kanjiList)):
                # print(kanjiList[i])
                csv_writer.writerow(kanjiList[i])
                i += 1
            else:
                break
        file_num += 1

i = 0
file_num = 0
while (file_num < (len(kanaList) / float(line_limit))):
    with open('jlpt/' + fileName + '-kana-' + str(file_num) + '.csv', 'w', encoding="utf-8", newline='') as f:
        csv_writer = csv.writer(f, delimiter=',')
        for x in range(line_limit):
            if (i < len(kanaList)):
                # print(kanaList[i])
                csv_writer.writerow(kanaList[i])
                i += 1
            else:
                break
        file_num += 1
