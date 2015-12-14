import numpy as np
import matplotlib.pyplot as plt

log = np.array(\
[['2015-05-08 15:46:06', '2015-05-08 17:21:36'],\
 ['2015-05-08 17:10:53', '2015-05-09 06:30:08'],\
 ['2015-08-09 22:38:45', '2015-08-09 22:38:45'],\
 ['2015-08-09 22:41:33', '2015-08-10 08:39:26'],\
 ['2015-08-11 17:25:52', '2015-08-12 08:14:30'],\
 ['2015-08-13 13:12:08', '2015-08-13 19:42:50'],\
 ['2015-08-13 17:30:18', '2015-08-14 10:13:10'],\
 ['2015-10-20 13:42:07', '2015-10-20 16:13:37'],\
 ['2015-10-21 10:27:05', '2015-10-21 16:13:11'],\
 ['2015-12-05 13:28:51', '2015-12-05 22:43:20']],\
 dtype="datetime64")



# INIT

# how to set this variable automatically (dt64 does not handle weekday)
begin = np.datetime64("2015-05-04")        # first monday
end = np.datetime64("2015-12-07")      # last monday

week_td64 = np.timedelta64(1, 'W')

nbWeek_td64 = int((end - begin) / week_td64)



# COMPUTE

week = begin + np.arange(nbWeek_td64) * week_td64
weekHours = []

# how to get rid of this loop
for w in week:

    mask1 = log[:,0] > w
    mask2 = log[:,0] < w  + week_td64
    l = log[mask1 & mask2]
    print l
    print l[:,0]
    print l[:,1]

    totalweek = (l[:,1] - l[:,0]).sum()

    weekHours.append(totalweek)

plt.plot(weekHours)
plt.show()
