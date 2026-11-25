#birthdays = {
    #'Albert Einstein': '03/14/1879',
    #'Benjamin Franklin': '01/17/1706',
    #'Ada Lovelace': '12/10/1815',
    #'Donald Trump': '06/14/1946',
    #'Rowan Atkinson': '01/6/1955',
     #'Manuel Marchiori' : '09/02/2005'}

import csv

def get_birthdays():
    new_dict = {}
    with open ("birthdays.csv", "r", newline="") as myfile:
        reader = csv.reader(myfile)
        next(reader)                     # salta la riga "Name,Birthday"
        for row in reader:
            new_dict[row[0]] = row[1]
    return new_dict


def return_birthday(name):
    '''Comment the function.'''
    birthdays = get_birthdays()
    if name in birthdays:
        return f"{name}'s birthday is {birthdays[name]}."
    return f"Sadly, we don't have {name}'s birthday."
        
