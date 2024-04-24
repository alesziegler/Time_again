
import datetime

print("Pro zadaný interval datumů vypíše všechny pátky 13.:")

print(datetime.datetime(2023, 3, 30))

first_date = datetime.datetime.strptime(input("Zadejte 1. datum (př. 1.1.2000):\n"),"%d.%m.%Y")

second_date = datetime.datetime.strptime(input("Zadejte 2. datum:\n"),"%d.%m.%Y")

anchor_date = first_date

while anchor_date <= second_date:
    print("test")
    if anchor_date.day == 13 and anchor_date.isoweekday() == 5:
        print("Friday 13th")
    anchor_date = anchor_date.replace(day=anchor_date.day+1)