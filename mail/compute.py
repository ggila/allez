import numpy as np
import pandas as pd
import datetime
import load

data = pd.DataFrame(load.heures, columns=['checkIn','checkOut'])

data.checkIn = data.checkIn.apply(lambda d: datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S'))
data.checkOut = data.checkOut.apply(lambda d: datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S'))

def getDay(d):
    return datetime.datetime(d.year, d.month, d.day)

data['dayIn'] = data['checkIn'].apply(getDay)
data['dayOut'] = data['checkIn'].apply(getDay)

data['lenght'] = data['checkOut'] - data['checkIn']
