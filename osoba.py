#import datetime

from datetime import datetime, timedelta

class Osoba:

  

  def __init__(self,birth_date):
    self.birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
    

  def birthday(self):
    birthday = datetime(datetime.today().year,self.birth_date.month,self.birth_date.day).date()
    return str(birthday)

  def how_old_they_are(self):
    #if birthdate_day+month lower than today, something
    #else something +/- 1
    pass