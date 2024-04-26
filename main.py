from osoba import Osoba

#from datetime import datetime

#random_date = datetime(datetime.today().year,5,12)

#print(random_date.date())

print("Zadejte datum narození: (př.: 1.1.2000)")
datumText = input()

someone = Osoba(datumText)

print(someone.birthday_2024())

print(someone.how_old_they_are())

print(someone.how_long_till_next_birthday())

print(f"Je ti {someone.how_old_they_are()} let a narozeniny máš za y dní.")