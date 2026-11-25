#! /usr/bin/env python3

import argparse

from bdpackage.bdmodule import get_birthdays, return_birthday

birthdays = get_birthdays()

firstnames = []
lastnames = []
for full_name in birthdays:
    first, last = full_name.split(" ", 1)
    firstnames.append(first)
    lastnames.append(last)

parser = argparse.ArgumentParser()
parser.add_argument("--firstname", required=True, choices=firstnames, help="Choose only names contained in the bdmodule file")
parser.add_argument("--lastname", required=True, choices=lastnames, help="Choose only surnmanes contained in the bdmodule fle")
args = parser.parse_args()

full_name = args.firstname + " " + args.lastname

print(return_birthday(full_name))

