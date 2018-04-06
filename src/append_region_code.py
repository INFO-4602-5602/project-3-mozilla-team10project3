import csv
from collections import defaultdict
import pandas as pd
import sys

country2region = {}
country2subregion = {}
region2subregion = defaultdict(set)
with open('../data/all.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['region'], row['sub-region'])
        country2region[row['name']] = row['region']
        country2subregion[row['name']] = row['sub-region']
        region2subregion[row['region']].add(row['sub-region'])

for k, v in sorted(region2subregion.items(), key=lambda x:len(x[1])):
    print(k, v)
sys.exit(1)

oov = set()
country_dic = defaultdict(int)
country2region["United Kingdom"] = "Europe"
country2subregion["United Kingdom"] = "Northern Europe"
country2region["USA"] = "Americas"
country2subregion["USA"] = "Northern America"

csv_file_read = open('../data/20171013111831-SurveyExport_TruncatedFields.csv', newline='', errors='ignore')
reader = csv.DictReader(csv_file_read)
for row in reader:
    country = row['Country']
    country_dic[country] += 1
    if not country in country2region:
        oov.add(country)
fieldnames = reader.fieldnames
fieldnames.append("Region")
fieldnames.append("Sub-Region")
#print(fieldnames)

csv_file_read = open('../data/20171013111831-SurveyExport_TruncatedFields.csv', newline='', errors='ignore')
reader = csv.DictReader(csv_file_read)
with open("../data/20171013111831-SurveyExport_TruncatedFields_Region.csv", "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for line in reader:
        country = line['Country']
        if not country in country2region:
            line['Region'] = None
            line['Sub-Region'] = None
        else:
            line['Region'] = country2region[country]
            line['Sub-Region'] = country2subregion[country]
        writer.writerow(line)
        #print(line)

print(len(set(country2region.values())))
print(set(country2region.values()))

#print(oov)
#for k, v in sorted(country_dic.items(), key=lambda x:x[1]):
#    print(k,v)
