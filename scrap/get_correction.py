import getpass
import mechanize
from bs4 import BeautifulSoup
import re

url = 'https://intrav2.42.fr'
url2 = 'https://profile.intrav2.42.fr/users/'

searched_class = 'block-item parent piscine-cpp project-item'

b = mechanize.Browser()
b.open(url)
b.select_form(nr=0)
print 'Entering' + url
login = raw_input('login : ')
pwd = getpass.getpass('password : ')
b['user[login]']=login
b['user[password]']=pwd
b.submit()
fd=open('./cpp.txt', 'r')
for line in fd:
    print line[:-1]
    fd=b.open(url2+line)
    soup = BeautifulSoup(fd.read(), 'html.parser')
    projects = soup.find_all('div', class_=searched_class)
    for p in projects:
        potage = BeautifulSoup(str(p), 'html.parser')
        print potage.find_all('a')[1].contents[0],
        print potage.span.span['data-long-date'],
        print str(potage.div.div.contents[0])[1:-1]
    print ' '
