import numpy as np
import pandas as pd
import datetime
import load

session = pd.DataFrame(load.sessions, columns=['checkIn','checkOut'])

session.checkIn = session.checkIn.apply(lambda d: datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S'))
session.checkOut = session.checkOut.apply(lambda d: datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S'))

def getDay(d):
    return datetime.datetime(d.year, d.month, d.day)

session['dayIn'] = session['checkIn'].apply(getDay)
session['dayOut'] = session['checkOut'].apply(getDay)

session['hourIn'] = session['checkIn'] - session['dayIn']
session['hourOut'] = session['checkOut'] - session['dayOut']

session['lenght'] = (session['checkOut'] - session['checkIn']).apply(np.timedelta64) / 3.6e9

begin = session['dayIn'][0]
end = session['dayOut'].iloc[-1] 
nbDay = np.timedelta64(end - begin) / np.timedelta64(1, 'D')

day = pd.DataFrame(np.datetime64(begin) + np.arange(nbDay) * np.timedelta64(1, 'D'), columns=['day'])

