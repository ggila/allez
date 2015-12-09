import re
import os
import time
import MailBox as MB
import matplotlib.pyplot as plt
import numpy as np

user = raw_input()

if not (os.path.exists(user)):    #check if user known
    mb = MB.MailBox(user)
    data = mb.getPattern(mb.getMailFrom('bigbrother'))
    pattern = '[0-9]{4}.{15}'
    heures = [re.findall(pattern, sess) for sess in session]

def decoupe(a):
    return a[1] - a[0]

hours = np.array(heures, dtype='datetime64')

begin = np.datetime64("2015-05-04")
end = np.datetime64("2015-12-07")

week_time = np.timedelta64(1, 'W')
nb_week = int((end - begin) / week_time)

week = begin + np.arange(nb_week) * week_time

l = []

for i, w in enumerate(week):
    mask1 = hours[:,0] > w
    mask2 = hours[:,0] < w  + week_time
    sess = hours[mask1 & mask2]
    l.append((sess[:,1] - sess[:,0]).sum())

week_hours = np.array(l) / 3600.0

plt.plot(week, week_hours, 'b+')

print week_hours.mean()

plt.show()
