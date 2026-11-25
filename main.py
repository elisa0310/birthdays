#! /usr/bin/env python3

import argparse

from bdpackage.bdmodule import return_birthday

parser = argparse.ArgumentParser()
parser.add_argument("--firstname", required=True, choices=['Albert','Benjamin','Ada','Donald','Rowan','Manuel'], help= "Choose only names contained in the bdmodule file")
parser.add_argument("--lastname", required=True, choices= ['Einstein','Franklin','Lovelace','Trump','Atkinson','Marchiori'], help= "Choose only surnmanes contained in the bdmodule fle")
args = parser.parse_args()

full_name = args.firstname + " " + args.lastname

return_birthday(full_name)

