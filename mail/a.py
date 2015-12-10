import re
import os
import datetime
import MailBox as MB
#import matplotlib.pyplot as plt
#import numpy as np

##
# Get Usr
##

user = raw_input('user: ')
if not user: user = 'gilabertgautier@gmail.com'

##
# Get Data
##

if not (os.path.exists(user)):      #check if user known
    mb = MB.MailBox(user)       #if not, get data from gmail
    data = mb.getPattern(mb.getMailFrom('bigbrother'))
    pattern = '[0-9]{4}.{15}'       # Get line with date of checkin checkout
    heures = [re.findall(pattern, sess) for sess in data]       #get formated data from mail
    with open(user, 'w') as f:      #save data
        for a, b in heures:
            f.write('{0}, {1}\n'.format(a, b))
else:                           #get data from file
    heures = []
    with open(user, 'r') as f:
        for line in f:
            heures.append(line[:-1].split(', '))


##
# Process Data
##

def castStrDate(sess):      #cast str to datetime.datetime
    return [datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S') for s in sess]

heures = map(castStrDate, heures)
heures = [[a, b, b-a] for a, b in heures]

def getDay(d):
    return datetime.datetime(d.year, d.month, d.day)

dataDay = []
dataWeek = []

begin = getDay(heures[0][0])
end = getDay(heures[-1][1])
day = begin

it = iter(heures)
checkIn, checkOut, delta = it.next()
weekWork = datetime.timedelta(0)

dayOf = [[], [], []]
NbOf = 0
isPrevDayOf = 0
while day <= end:
    dayWork = datetime.timedelta(0)
    while day == getDay(checkIn):
        if day == getDay(checkOut):
            dayWork = dayWork + delta
            try:
                checkIn, checkOut, delta = it.next()
            except:
                checkIn = day + datetime.timedelta(1)
        else:
            nextDay = day + datetime.timedelta(1)
            dayWork = dayWork + (nextDay - checkIn)
            delta = delta - dayWork
            checkIn = nextDay

    weekWork += dayWork
    dataDay.append(dayWork)

    if dayWork == datetime.timedelta(0):
        NbOf += 1
        if isPrevDayOf == 0:
            dayOf[0].append(day)
            isPrevDayOf = 1
    else:
        if isPrevDayOf != 0:
            isPrevDayOf = 0
            dayOf[1].append(NbOf)
        NbOf = 0
    dayOf[2].append(isPrevDayOf)

    if day.weekday() == 6:
        dataWeek.append(weekWork)
        weekWork = datetime.timedelta(0)

    day += datetime.timedelta(1)


firstWeekLen = 1
d = begin
while (d.weekday() != 6):
    firstWeekLen += 1
    d += datetime.timedelta(1)

lastWeekLen = 1
d = end
while (d.weekday() != 0):
    lastWeekLen += 1
    d -= datetime.timedelta(1)

#hours = np.array(heures, dtype='datetime64')
#
#begin = np.datetime64("2015-05-04")
#end = np.datetime64("2015-12-07")
#
#week_time = np.timedelta64(1, 'W')
#nb_week = int((end - begin) / week_time)
#
#week = begin + np.arange(nb_week) * week_time
#
#l = []
#
#for i, w in enumerate(week):
#    mask1 = hours[:,0] > w
#    mask2 = hours[:,0] < w  + week_time
#    sess = hours[mask1 & mask2]
#    l.append((sess[:,1] - sess[:,0]).sum())
#
#week_hours = np.array(l) / 3600.0
#
#plt.plot(week, week_hours, 'b+')
#
#print week_hours.mean()
#
#plt.show()
