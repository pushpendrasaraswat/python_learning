import datetime as dt


now = dt.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.weekday()) # Monday is 0 and Sunday is 6


date_of_birth = dt.date(year=2020, month=12, day=31)

print(date_of_birth)
