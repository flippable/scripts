#!/usr/bin/env python

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
import csv

BASEURL = 'https://openstates.org/api/v1/legislators/'

OUTPUT_FILENAME = 'legislators.csv'

LEG_ID = 'Legislator ID'
STATE = 'State'
CHAMBER = 'Chamber'
DISTRICT = 'District'
PARTY = 'Party'
FIRST_NAME = 'First Name'
LAST_NAME = 'Last Name'
EMAIL = 'Email'
PHONE = 'Phone'

FIELDNAMES = [
    LEG_ID,
    STATE,
    CHAMBER,
    DISTRICT,
    PARTY,
    FIRST_NAME,
    LAST_NAME,
    EMAIL,
    PHONE
]

def write_data(leg_list, filepath):
    with open(filepath, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES, delimiter="\t")
        writer.writeheader()
        for value in leg_list:
            writer.writerow(value)

def main():
    response = requests.get(BASEURL)
    data = response.json()
    legislators = []

    for entry in data:
        legislator = {
            LEG_ID: entry.get('leg_id', '-'),
            STATE: entry.get('state', '-').upper(),
            CHAMBER: entry.get('chamber', '-').title(),
            DISTRICT: entry.get('district', '-'),
            PARTY: entry.get('party', '-'),
            EMAIL: entry.get('email', '-'),
            FIRST_NAME: entry.get('first_name', '-'),
            LAST_NAME: entry.get('last_name', '-')
        }

        if entry.get('offices'):
            if legislator[EMAIL] == '-':
                legislator[EMAIL] = entry.get('offices')[0].get('email', '-')
            legislator[PHONE] = entry.get('offices')[0].get('phone', '-')

        legislators.append(legislator)

    write_data(legislators, OUTPUT_FILENAME)

if __name__ == '__main__':
    main()
