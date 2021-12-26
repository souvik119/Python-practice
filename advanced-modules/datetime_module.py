import datetime
from datetime import datetime
from datetime import date

# TIME OBJECT
# mytime = datetime.time(2, 20) # 20 minute past 2 am
# print(mytime.minute)
# print(mytime.hour)
# print(mytime)
# print(type(mytime)) # it is datetime.time object only holds values of time not date

# DATE OBJECT
# today = datetime.date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(type(today))
# #use a different format
# print(today.ctime())

# DATETIME OBJECT
# mydatetime = datetime(2021, 12, 26, 23, 32, 23) # year, month, day, hour , minute, seconds
# print(mydatetime)
# #say you want to change an attribute
# mydatetime = mydatetime.replace(year=2020) # does not happen in place, have to assign
# print(mydatetime)

# ARITHMETIC on date, time
date1 = date(2021, 12, 26)
date2 = date(2020, 12, 26)
result = date1 - date2
print(result.days)
print(type(result))

datetime1 = datetime(2021, 12, 26, 23, 45)
datetime2 = datetime(2020, 12, 26, 11, 45)
result = datetime1 - datetime2
print(result)
print(result.total_seconds())
print(type(result))