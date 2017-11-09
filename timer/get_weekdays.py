# coding:utf-8

import datetime

def get_birthday_weekday(birthday_str=None):
    weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    if birthday_str == None:
        birthday=datetime.datetime.today()
        birthday_str=str(datetime.date.today())
    else:
        birthday=datetime.datetime.strptime(birthday_str,'%Y-%m-%d')

    print('Your birthday {0} is {1}'.format(birthday_str,weekdays[birthday.weekday()]))

gf_birthday='2017-09-07'
bf_birthday='2017-3-3'
get_birthday_weekday(gf_birthday)
get_birthday_weekday(bf_birthday)