import load
import numpy as np
import matplotlib.pyplot as plt

def GetMonday(firstDay, way='forward'):
    firstEntry = firstDay.astype('M8[D]')
    beforeMonday = np.busday_offset(firstEntry, 0, way, [1,0,0,0,0,0,0])
    if abs(firstEntry-beforeMonday) == np.timedelta64(7, 'D'):
        return firstEntry.astype('M8[s]')
    else:
        return beforeMonday.astype('M8[s]')

# Process Data

log = np.array(load.sessions, dtype='datetime64') # load data

# init some const

begin = GetMonday(np.min(log.flatten()), way='backward')
end = GetMonday(np.max(log.flatten()))

n_logs = log.shape[0]*1.0
week_td64 = np.timedelta64(1, 'W')

weeks_entry = np.floor((log[:,0]-begin)/week_td64)
hours_spent = (log[:,1]-log[:,0]).astype('timedelta64[m]')

week_hours = np.bincount(weeks_entry.astype('int64'), hours_spent.astype('float64') / 60)

plt.plot(np.arange(begin, end, week_td64), week_hours, 'b')

plt.show()
