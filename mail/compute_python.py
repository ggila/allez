import load

session = pd.DataFrame(load.heures, columns=['checkIn','checkOut'])

##
# Process Data
##

def castStrDate(sess):      #cast str to datetime.datetime
    return [datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S') for s in sess]

sessions = map(castStrDate, heures)
sessions = [[a, b, b-a] for a, b in sessions]  sessions = checkIn, checkOut, lenght

dataDay = []
dataWeek = []

begin = getDay(sessions[0][0])
end = getDay(sessions[-1][1])
day = begin

it = iter(sessions)
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

#hours = np.array(sessions, dtype='datetime64')
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
