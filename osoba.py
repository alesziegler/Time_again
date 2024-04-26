#import datetime

from datetime import datetime, timedelta

from calendar import isleap

class Osoba:

  

  def __init__(self,birth_date):
    self.birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
    

  def birthday_2024(self):
    birthday_2024 = datetime(datetime.today().year,self.birth_date.month,self.birth_date.day)#.date()
        
    return birthday_2024

  def how_old_they_are(self):
    # this works when birthdays in 2024 are before now:
    if self.birthday_2024() < datetime.today():
      age = self.birthday_2024().year - self.birth_date.year
    else:
      age = (self.birthday_2024().year - self.birth_date.year) - 1
    
    return age
    