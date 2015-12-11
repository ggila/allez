import load
import numpy as np
import matplotlib.pyplot as plt

# Process Data

sessions = np.array(load.sessions, dtype='datetime64') # load data

# init some const

begin_dt64 = np.datetime64("2015-05-04") # first monday
end_dt64 = np.datetime64("2015-12-07") # last monday

week_td64 = np.timedelta64(1, 'W')

nbWeek_td64 = int((end_dt64 - begin_dt64) / week_td64)

week = begin_dt64 + np.arange(nbWeek_td64) * week_td64 # array of week

weekHours = []


for w in week:
    mask1 = sessions[:,0] > w
    mask2 = sessions[:,0] < w  + week_td64
    sess = sessions[mask1 & mask2]
    weekHours.append((sess[:,1] - sess[:,0]).sum())

weekHours = np.array(weekHours) / 3600.0

plt.plot(week, weekHours, 'b+')

plt.show()
