import numpy as np
import matplotlib.pyplot as plt

log =\
[['2015-05-08 15:46:06', '2015-05-08 17:21:36'],\
 ['2015-05-08 17:10:53', '2015-05-09 06:30:08'],\
 ['2015-08-09 22:38:45', '2015-05-09 22:38:45'],\
 ['2015-08-09 22:41:33', '2015-05-10 08:39:26'],\
 ['2015-08-11 17:25:52', '2015-05-12 08:14:30'],\
 ['2015-08-13 13:12:08', '2015-05-13 19:42:50'],\
 ['2015-08-13 17:30:18', '2015-05-14 10:13:10'],\
 ['2015-10-20 13:42:07', '2015-05-20 16:13:37'],\
 ['2015-10-21 10:27:05', '2015-05-21 16:13:11'],\
 ['2015-12-05 13:28:51', '2015-05-23 22:43:20']]

log = np.array(log, dtype='datetime64') # load data

# INIT

# how to set this variable automatically (dt64 does not handle weekday)
begin_dt64 = np.datetime64("2015-05-04") # first monday
end_dt64 = np.datetime64("2015-12-07") # last monday

week_td64 = np.timedelta64(1, 'W')

nbWeek_td64 = int((end_dt64 - begin_dt64) / week_td64)

# time range
week = begin_dt64 + np.arange(nbWeek_td64) * week_td64

weekHours = []

# how to get rid of this loop
for w in week:
    mask1 = log[:,0] > w
    mask2 = log[:,0] < w  + week_td64
    l = log[mask1 & mask2]
    weekHours.append((l[:,1] - l[:,0]).sum())
