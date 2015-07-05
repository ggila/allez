import getpass
import mechanize
import re

url = 'http://duoquadragintien.fr'

fd=open('hours_all.txt', 'w')

pattern = re.compile('2015-6-\d\d 00:00:00 \+0100":([0-9.]+)')

print 'Connecting to ' + url
login = raw_input('login : ')
pwd = getpass.getpass('password : ')

b = mechanize.Browser()
b.open(url)
b.select_form(nr=0)
b['login'] = login
b.submit()
b.select_form(nr=0)
b['password'] = pwd
b.submit()

with open('student.txt', 'r') as f:
    for line in f:
        b.select_form(nr=0)
        b['login'] = line[:-1]
        data = b.submit().read()
        r = re.finditer(pattern, data)
        fd.write(line[:-1])
        for i in range(8):
            elem = next(r)
            fd.write(' ' + elem.group(1))
        fd.write('\n')

fd.close()
