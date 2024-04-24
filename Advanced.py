
import datetime

print("Pro zadaný interval datumů vypíše všechny pátky 13.:")

first_date = datetime.datetime.strptime(input("Zadejte 1. datum (př. 1.1.2000):\n"),"%d.%m.%Y")

second_date = datetime.datetime.strptime(input("Zadejte 2. datum:\n"),"%d.%m.%Y")

anchor_date = first_date

fridays_13th = ""

while anchor_date <= second_date:
    #print("test")
    if anchor_date.day == 13 and anchor_date.isoweekday() == 5:
        fridays_13th += f"{str(anchor_date.date())}, "
    anchor_date += datetime.timedelta(days=1)
print(f"Patky 13: {fridays_13th}")