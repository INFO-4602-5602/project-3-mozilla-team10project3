#!/usr/bin/env python3

import csv

_NATIONAL = {}
_DEFAULT = {
    'botnet' : 0,
    'blockchain' : 0,
    'ddos' : 0,
    'zeroday' : 0,
    'rfid' : 0,
    'vpn' : 0,
    'tor' : 0,
    'total' : 0
}

_K_COUNTRY = 'Country'
_K_BOTNET = 'Botnet:Check all the terms below that you could explain to a friend:'
_K_BLOCKCHAIN = 'Blockchain:Check all the terms below that you could explain to a friend:'
_K_DDOS = 'DDOS:Check all the terms below that you could explain to a friend:'
_K_ZERODAY = 'Zero Day:Check all the terms below that you could explain to a friend:'
_K_RFID = 'RFID:Check all the terms below that you could explain to a friend:'
_K_VPN = 'VPN:Check all the terms below that you could explain to a friend:'
_K_TOR = 'TOR:Check all the terms below that you could explain to a friend:'


if __name__ == '__main__':
    with open('../data/20171013111831-SurveyExport_TruncatedFields_Region.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            nation = line[_K_COUNTRY]
            btnt = 1 if line[_K_BOTNET] == 'Botnet' else 0
            bchn = 1 if line[_K_BLOCKCHAIN] == 'Blockchain' else 0
            ddos = 1 if line[_K_DDOS] == 'DDOS' else 0
            zday = 1 if line[_K_ZERODAY] == 'Zero Day' else 0
            vpn = 1 if line[_K_VPN] == 'VPN' else 0
            tor = 1 if line[_K_TOR] == 'TOR' else 0
            rfid = 1 if line[_K_RFID] == 'RFID' else 0
            try:
                _NATIONAL[nation]
            except KeyError:
                _NATIONAL[nation] = _DEFAULT
            _NATIONAL[nation]['botnet'] += btnt
            _NATIONAL[nation]['blockchain'] += bchn
            _NATIONAL[nation]['ddos'] += ddos
            _NATIONAL[nation]['zeroday'] += zday
            _NATIONAL[nation]['rfid'] += vpn
            _NATIONAL[nation]['vpn'] += tor
            _NATIONAL[nation]['tor'] += rfid
            _NATIONAL[nation]['total'] += 1
    print(_NATIONAL)
