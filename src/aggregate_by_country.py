import csv
from collections import defaultdict
import pandas as pd
# Country,Percentage,Savvy

# excited.csv
# optimistic.csv
# fence.csv
# warry.csv
# scared.csv

# CSV_nameExcited,Optimisitc,Fence,Warry,Scared,
out_file_dic = {}
f_exicted = open("excited.csv", "w")
out_file_dic["Sup"] = f_exicted
f_optimistic = open("optimistic.csv", "w")
out_file_dic["Cau"] = f_optimistic
f_fence = open("fence.csv", "w")
out_file_dic["On "] = f_fence
f_warry = open("warry.csv", "w")
out_file_dic["A l"] = f_warry
f_scared = open("scared.csv", "w")
out_file_dic["Sca"] = f_scared

for k, v in out_file_dic.items():
    v.write("Country,Percentage,Savvy\n")




def process_column(field_name, field_dic, region):
    if field_name:
        field_dic[region] += 1

#country_responses = defaultdict(int)
country_responses = defaultdict(int)
country_responses_breakdown = defaultdict(lambda: defaultdict(int))
country_responses_breakdown_techsavvy_score = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
savvy_score_dic = {'Ultra Nerd': 3, 'Technically Savvy': 2, 'Average User': 1, 'Luddite': 0}

csv_file_read = open('../data/20171013111831-SurveyExport_TruncatedFields_Region.csv', newline='', errors='ignore')
reader = csv.DictReader(csv_file_read)
for row in reader:
    country= row['Country']
    ans = row['Thinking about a future in which so much of your world is connected to the internet leaves you feeling:']
    date = row['Date Submitted']
    tech_savvy = row['I consider myself:']

    if (not ans) or (not tech_savvy): 
        continue
    
    country_responses[country] += 1
    country_responses_breakdown[country][ans] += 1
    country_responses_breakdown_techsavvy_score[country][ans][tech_savvy] += 1

#for k, v in brazil.items():
#    total_country = sum(brazil.values())
#    print("total responses: %i" % (total_country))
#    print(k, v/total_country)

print("Num. of countries: %i" % (len(country_responses)))
for k, v in sorted(country_responses.items(), key=lambda x:x[1], reverse=True)[:50]:
    #print(k, v)
    #print(country_responses_breakdown[k])
    #if k == "India":
    for response, nums in country_responses_breakdown[k].items():
        sum_savvy_score = 0
        sum_savvy_people = 0
        percentage = nums/v
        #print(response, nums/v)
        for savvy, savvy_people in country_responses_breakdown_techsavvy_score[k][response].items():
            sum_savvy_score += savvy_score_dic[savvy] * savvy_people
            sum_savvy_people += savvy_people
        print("India avg. savvy score for response '%s': %.4f" % (response, sum_savvy_score/sum_savvy_people))
        out_file_dic[response[:3]].write("%s" % (k))
        out_file_dic[response[:3]].write(",%.4f" % (percentage))
        out_file_dic[response[:3]].write(",%.4f" % (sum_savvy_score/sum_savvy_people))
        out_file_dic[response[:3]].write("\n")



            
            #print(country_responses_breakdown_techsavvy_score[k][response])
