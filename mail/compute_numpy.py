import load
import numpy as np
import matplotlib.pyplot as plt

##
# Process Data
##

sessions = np.array(load.sessions, dtype='datetime64') # load data (check module load)

#init some const
begin = np.datetime64("2015-05-04")
end = np.datetime64("2015-12-07")

week_time = np.timedelta64(1, 'W')

nb_week = int((end - begin) / week_time)

week = begin + np.arange(nb_week) * week_time #array of week

l = []


for i, w in enumerate(week):
    mask1 = sessions[:,0] > w
    mask2 = sessions[:,0] < w  + week_time
    sess = sessions[mask1 & mask2]
    l.append((sess[:,1] - sess[:,0]).sum())

week_sessions = np.array(l) / 3600.0

plt.plot(week, week_sessions, 'b+')

plt.show()
