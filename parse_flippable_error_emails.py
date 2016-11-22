# -*- coding: utf-8 -*-
""" Quick and dirty script to parse bad form submissions into CSV.

	How to run:
		python parse_flippable_error_emails.py flippable-errors.txt
		where flippable-error-emails.txt is a dump of the bad form submission emails.
"""

import csv
import sys


EMAIL = 'email address'
NAME = 'name'
ZIPCODE = 'zip code'

FIELDNAMES = [
    EMAIL,
    NAME,
    ZIPCODE,
]

OUTPUT_FILENAME = 'flippable-errors.csv'


def main(input_filepath, output_filepath=OUTPUT_FILENAME):
    print 'reading in user data from ', input_filepath
    user_data_dict = read_in_user_data(input_filepath)
    print 'read in data for ', len(user_data_dict), 'users'

    print 'writing user data to CSV ', output_filepath
    write_user_data(user_data_dict, output_filepath)


def write_user_data(user_data_dict, filepath):
    """ Writes values of user data dict to filepath """
    with open(filepath, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()

        for key, row in user_data_dict.iteritems():
            writer.writerow(row)


def read_in_user_data(input_filepath):
    """ Returns dict of dicts of format
        {email: {'email address': email, 'name': name, 'zip code': zipcode}}
        where email is used as key to avoid duplicates
    """
    user_data_dict = {}
    with open(input_filepath, 'r') as my_file:
        data_dump = my_file.read()
        split_dump_list = data_dump.split('Here is a copy of the submission for your records:')[1:]

        for i, user_data_dump in enumerate(split_dump_list):
            email = _parse_user_data(user_data_dump, EMAIL)
            name = _parse_user_data(user_data_dump, NAME)
            zipcode = _parse_user_data(user_data_dump, ZIPCODE)

            user_data_dict[email] = {
                EMAIL: email,
                NAME: name,
                ZIPCODE: zipcode
            }

    return user_data_dict


def _parse_user_data(user_data, fieldname):
    """ Returns fieldname value in ugliest way possible to parse """
    return user_data.split(fieldname + ': \n')[1].split('\n')[0].strip()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'ERROR: expected filepath to form submissions error dump'

    else:
        main(sys.argv[1])
