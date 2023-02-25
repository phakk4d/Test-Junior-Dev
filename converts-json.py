import csv
import json
import codecs

with open ("original_database_from_thaipost.csv", "r", encoding='utf-8') as f :
    reader = csv.reader(f)

    data = []
    for row in reader :
        data.append({'PROVINCE_ID': row[0], 'PROVINCE_NAME' : row[1] , 'BORDER_ID' : row[2], 'BORDER_NAME' : row[3], 'BORDER_POSTAL_CODE' : row[4], 'DISTRICT_ID' : row[5], 'DISTRICT_NAME' : row[6], 'DISTRICT_POSTAL_CODE' : row[7]})
        #print (data)


with open ("new_database.json", "w", encoding='utf-8') as f :
    json.dump(data, f, indent=4, ensure_ascii=False)