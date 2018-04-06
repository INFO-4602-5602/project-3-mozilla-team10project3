#!/usr/bin/env python3

import csv
import pprint

from iso3166 import countries

pprint = pprint.PrettyPrinter(indent=2).pprint

_CSV_IN = '../data/20171013111831-SurveyExport_TruncatedFields_Region.csv'
_CSV_OUT = '../vis-interactive-map/national_aggregates.csv'

_NATIONAL = {}
_DEFAULT = {
    'botnet' : 0,
    'blockchain' : 0,
    'ddos' : 0,
    'zday' : 0,
    'rfid' : 0,
    'vpn' : 0,
    'tor' : 0,
    'iot' : 0,
    'condev' : 0,
    'total' : 0
}

# I don't know if this is because the Mozilla data is wrong or
# if the ISO 3166 library I imported above sucks
_EXCEPTIONS = {
    'United Kingdom' : 'United Kingdom of Great Britain and Northern Ireland',
    'Bolivia' : 'Bolivia, Plurinational State of',
    'Macau' : 'Macao',
    "Cote D'Ivoire" : "Côte d'Ivoire",
    'Venezuela' : 'Venezuela, Bolivarian Republic of',
    'Reunion' : 'Réunion',
    'Macedonia' : 'Macedonia, the former Yugoslav Republic of',
    'Czech Republic' : 'Czechia',
    'Palestinian Territory' : 'Palestine',
    #This one makes me the most upset
    'Congo, The Democratic Republic of the' : 'Congo, Democratic Republic of the',
    'Curacao' : 'Curaçao',
    'Vietnam' : 'Viet Nam',
    'Saint Martin' : 'Sint Maarten (Dutch part)',
    'Cape Verde' : 'Cabo Verde',
    'Holy See (Vatican City State)' : 'Holy See'

}

_K_COUNTRY = 'Country'
_K_BOTNET = 'Botnet:Check all the terms below that you could explain to a friend:'
_K_BLOCKCHAIN = 'Blockchain:Check all the terms below that you could explain to a friend:'
_K_DDOS = 'DDOS:Check all the terms below that you could explain to a friend:'
_K_ZERODAY = 'Zero Day:Check all the terms below that you could explain to a friend:'
_K_RFID = 'RFID:Check all the terms below that you could explain to a friend:'
_K_VPN = 'VPN:Check all the terms below that you could explain to a friend:'
_K_TOR = 'TOR:Check all the terms below that you could explain to a friend:'
_K_CONDEV = 'Connected Devices:Check all the terms below that you could explain to a friend:'
_K_IOT = 'IoT:Check all the terms below that you could explain to a friend:'

_THRESH = 100

if __name__ == '__main__':
    with open(_CSV_IN, 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            cn = line[_K_COUNTRY]
            try:
                nation = countries.get(cn).alpha3
            except KeyError:
                try:
                    nation = countries.get(_EXCEPTIONS[cn]).alpha3
                except KeyError:
                    print("[DEBUG] Skipping invalid or unknown country ", cn)
                    continue
            btnt = 1 if line[_K_BOTNET] == 'Botnet' else 0
            bchn = 1 if line[_K_BLOCKCHAIN] == 'Blockchain' else 0
            ddos = 1 if line[_K_DDOS] == 'DDOS' else 0
            zday = 1 if line[_K_ZERODAY] == 'Zero Day' else 0
            vpn = 1 if line[_K_VPN] == 'VPN' else 0
            tor = 1 if line[_K_TOR] == 'TOR' else 0
            rfid = 1 if line[_K_RFID] == 'RFID' else 0
            iot = 1 if line[_K_IOT] == 'IoT' else 0
            condev = 1 if line[_K_CONDEV] == 'Connected Devices' else 0
            try:
                _NATIONAL[nation]
            except KeyError:
                _NATIONAL[nation] = _DEFAULT.copy()
            _NATIONAL[nation]['botnet'] += btnt
            _NATIONAL[nation]['blockchain'] += bchn
            _NATIONAL[nation]['ddos'] += ddos
            _NATIONAL[nation]['zday'] += zday
            _NATIONAL[nation]['rfid'] += rfid
            _NATIONAL[nation]['vpn'] += vpn
            _NATIONAL[nation]['tor'] += tor
            _NATIONAL[nation]['iot'] += iot
            _NATIONAL[nation]['condev'] += condev
            _NATIONAL[nation]['total'] += 1
    filtered = { k: v for k,v in _NATIONAL.items() if v['total'] > _THRESH}
    print(len(filtered.keys()))
    #pprint(filtered)

    def row_into(k,v):
        newv = v.copy()
        newv['iso'] = k
        return newv

    fieldnames = ['iso', 'botnet', 'blockchain', 'ddos', 'zday', 'rfid', 'vpn', 'tor', 'iot', 'condev', 'total']
    data = [row_into(k,v) for k,v in filtered.items()]
    with open(_CSV_OUT, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("All done!")
