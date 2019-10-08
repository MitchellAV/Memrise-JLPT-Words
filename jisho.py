import requests
import json

level = 3
page = 1
# str(level)
term = 'jlpt-n3'
url = "https://jisho.org/api/v1/search/words?keyword=%23"+ term +"&page="
data = {"data":[]}
valid = True

while(valid):
    r = requests.get(url+str(page))
    if (r.status_code == 200):
        r = r.json()
        if (r["data"] != []):
            for value in r["data"]:
                data["data"].append(value)
            print(page)
        else:
            valid = False
            print("No data remaining")
    else:
        valid = False
        print("Status code not 200.")
    page += 1
print('Finished !!!')
with open(term +'.json', 'w', encoding='utf-8') as outfile:
    json.dump(data,outfile, ensure_ascii=False, indent=4)
