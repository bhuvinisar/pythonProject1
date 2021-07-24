import datetime

a = datetime.datetime.now()
print(a)
b= datetime.datetime.utcnow()
print(b)
d=datetime.date.today()
print(d)

from dateutil.relativedelta import relativedelta
a+=relativedelta(days=2)


print(a)

from datetime import timedelta
a+=timedelta(hours=5)
print(a)

import calendar
x=2000
y=12
print(calendar.month(x,y))