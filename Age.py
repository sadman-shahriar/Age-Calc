#-------- Don't Change Source ----------#
#-------- Sadman Shahriar ----------#

import datetime
import jdatetime



def out(o):
    with open('Age.txt', 'w+') as out:
        cp = '-- Programming By Alireza nori --'
        out.write(f'{o}\n{cp}')


class Age(object):
    def __init__(self, age_date):
        self.age = age_date
        self.datetime = datetime
        self.jdatetime = jdatetime

    def date_miladi(self):
        age = self.age
        date = self.datetime.datetime.now()
        year = date.year - age
        month = (year*12) - date.month
        day = (month*365) - date.day
        hour = (day*12) - date.hour
        minute = (hour*60) - date.minute
        sec = (minute*1000) - date.second
        end = f'Year > {year}\nmonth > {month}\nday > {day}\nminute > {minute}\nsec > {sec}\n'.upper()
        print(end)

        if year < 50:
            print('Yong men')
        elif year >= 50:
            print('Old men Time to for dead!')
        return end

    def date_shamsi(self):
        date = self.jdatetime.datetime.now()
        year = date.year - self.age
        month = (year * 12) - date.month
        day = (month*365) - date.day
        hour = (day*12) - date.hour
        minute = (hour*60) - date.minute
        sec = (minute*1000) - date.second
        annn =f'Year > {year}\nmonth > {month}\nday > {day}\nminute > {minute}\nsec > {sec}\n'.upper()
        print(annn)
        if year < 50:
            print('Yong men')
        elif year >= 50:
            print('Old men Time to for dead!')
        return annn


def cp():
    cc = '-- Programming By Alireza Nori --'
    return cc


while True :
    try:
        jd = jdatetime.datetime.now().year
        age = int(input("Enter Your Age > "))
        print('   -- Hello Welcome to Age Calculator --\n   --HELP--\n- Send Your birthday Year\n')
        a = Age(age)
        if age > jd:
            yy = a.date_miladi()
            print(yy)
            print('Do you want to print Result ? y or n or yes or no')
            answer = input('> ')
            if answer == 'y' or 'yes':
                out(yy)
            if answer == 'n' or 'no':
                print('Good Bye!')
        elif age < jd:
            a.date_shamsi()
            yy = a.date_miladi()
            print(yy)
            print('Do you want to print Result ? y or n or yes or no')
            answer = input('> ')
            if answer == 'y' or 'yes':
                out(yy)
            if answer == 'n' or 'no':
                print('Good Bye!')
    except Exception as exp:
        print(f'Your Error --> {exp}')
    finally:

        print(cp())

#-------- Don't Change Source ----------#
#-------- Sadman Shahriar ----------#
