import re
import os
import datetime
import MailBox as MB
import matplotlib.pyplot as plt
import numpy as np

def cast(sess):
    return [datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S') for s in sess]

user = raw_input('user: ')
if not user: user = 'gilabertgautier@gmail.com'

if not (os.path.exists(user)):    #check if user known
    mb = MB.MailBox(user)         #if not, get data from gmail
    data = mb.getPattern(mb.getMailFrom('bigbrother'))
    pattern = '[0-9]{4}.{15}'
    heures = [re.findall(pattern, sess) for sess in data] #get formated data from mail
    with open(user, 'w') as f:   #save data
        for a, b in heures:
            f.write('{0}, {1}\n'.format(a, b))


heures = []

with open(user, 'r') as f:
    for line in f:
        heures.append(line[:-1].split(', '))
heures = map(cast, heures)
heures = [[a, b, b-a] for a, b in heures]


def getDay(d):
    return datetime.datetime(d.year, d.month, d.day)

begin = getDay(heures[0][0])
end = getDay(heures[-1][1])

#def decoupe(a):
#    return a[1] - a[0]
#
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
