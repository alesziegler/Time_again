
import datetime

print("Vypisuji součty cifer v datu pro následujících 9 dní:")

counter = 0
manipulated_date = datetime.datetime.now().date()

def date_sum(d):
    numbers = str(d).split("-")
    result = 0
    for number in numbers:
        result += int(number)
    return result

while counter <= 7:
    try:
        print(manipulated_date, end= " ")
        print(date_sum(manipulated_date))
        manipulated_date = manipulated_date.replace(day=manipulated_date.day+1)
    except:
        manipulated_date = manipulated_date.replace(month=manipulated_date.month+1,day=1)

    counter += 1
