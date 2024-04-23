
import datetime

print("Vypisuji součty cifer v datu pro následujících 7 dní:")

counter = 0
manipulated_date = datetime.datetime.now().date()


while counter <= 7:
    try:
        print(manipulated_date)
        manipulated_date = manipulated_date.replace(day=manipulated_date.day+1)
    except:

        print("overflow")
    counter += 1