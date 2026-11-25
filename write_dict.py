import csv

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955',
     'Manuel Marchiori' : '09/02/2005'}


with open ("birthdays.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Birthday"])
    for name, date in birthdays.items():
        writer.writerow([name, date])
