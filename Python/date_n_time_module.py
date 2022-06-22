from datetime import *

Time = datetime.now()
Date = date.today()
Year = date.today()

print(Time)
print(Date)
print(Year.year)
print(Year.month)
print(Year.day)
print(Time.hour)
print(Time.minute)
print(Time.second)

time = datetime(year=2010, day=21, month=10, hour=15, minute=20, second=10)

print(time)

timedif = Time - time
print(timedif)
