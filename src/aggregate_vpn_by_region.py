import csv
from collections import defaultdict
import pandas as pd

def process_column(field_name, field_dic, region):
    if field_name:
        field_dic[region] += 1

region_dic = defaultdict(int)
vpn_dic = defaultdict(int)
ddos_dic = defaultdict(int)
iot_dic = defaultdict(int)
cd_dic = defaultdict(int)
bot_dic = defaultdict(int)
blockchain_dic = defaultdict(int)
rfid_dic = defaultdict(int)
zero_day_dic = defaultdict(int)
tor_dic = defaultdict(int)

csv_file_read = open('../data/20171013111831-SurveyExport_TruncatedFields_Region.csv', newline='', errors='ignore')
reader = csv.DictReader(csv_file_read)
for row in reader:
    region = row['Sub-Region']
    vpn = row['VPN:Check all the terms below that you could explain to a friend:']
    ddos = row['DDOS:Check all the terms below that you could explain to a friend:']
    iot = row['IoT:Check all the terms below that you could explain to a friend:']
    cd = row['Connected Devices:Check all the terms below that you could explain to a friend:']
    bot = row['Botnet:Check all the terms below that you could explain to a friend:']
    blockchain = row['Blockchain:Check all the terms below that you could explain to a friend:']
    rfid = row['RFID:Check all the terms below that you could explain to a friend:']
    zero_day = row['Zero Day:Check all the terms below that you could explain to a friend:']
    tor = row['TOR:Check all the terms below that you could explain to a friend:']
    #print(region, vpn)
    region_dic[region] += 1
    process_column(ddos, ddos_dic, region)
    process_column(vpn, vpn_dic, region)
    process_column(iot, iot_dic, region)
    process_column(cd, cd_dic, region)
    process_column(bot, bot_dic, region)
    process_column(blockchain, blockchain_dic, region)
    process_column(rfid, rfid_dic, region)
    process_column(zero_day, zero_day_dic, region)
    process_column(tor, tor_dic, region)

with open("region_vpn.csv", "w") as csv_file:
    csv_file.write("Sub-Region,VPN,DDOS,IoT,Connected Devices,Botnet,Blockchain,RFID,Zero Day,TOR\n")
    for region in region_dic:
        vals = [vpn_dic[region], ddos_dic[region], iot_dic[region], cd_dic[region], bot_dic[region], blockchain_dic[region], rfid_dic[region], zero_day_dic[region], tor_dic[region]]
        out = map(lambda x:x/region_dic[region], vals)
        csv_file.write("%s" % (region))
        for val in out:
            csv_file.write(",%.4f" % (val))
        csv_file.write("\n")
