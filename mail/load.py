import re
import os
import datetime
import MailBox as MB

##
# Get Usr
##

user = raw_input('user: ')
if not user: user = 'gilabertgautier@gmail.com'

##
# Get Data
##

if not (os.path.exists(user)):      #check if user known
    mb = MB.MailBox(user)       #if not, get data from gmail
    data = mb.getPattern(mb.getMailFrom('bigbrother'))
    pattern = '[0-9]{4}.{15}'       # Get line with date of checkin checkout
    sessions = [re.findall(pattern, sess) for sess in data]       #get formated data from mail
    with open(user, 'w') as f:      #save data
        for a, b in sessions:
            f.write('{0}, {1}\n'.format(a, b))
else:                           #get data from file
    sessions = []
    with open(user, 'r') as f:
        for line in f:
            sessions.append(line[:-1].split(', '))
