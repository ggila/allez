import mechanize
import re

url = 'https://duoquadragintien.fr'

fd=open('hours.txt', 'w')

pattern = re.compile('<td>Jun \d\d, 2015, \d:\d\d:\d\d [AP]M</td><td>([\d.]+)<')

b = mechanize.Browser()
b.open(url)
b.select_form(nr=0)
b['login']='ggilaber'
b.submit()
b.select_form(nr=0)
b['password']=
b.submit()

for piscine in ['php','cpp','ocaml','unity']:
    with open('./' + piscine + '.txt', 'r') as f:
        for line in f:
            b.select_form(nr=0)
            b['login'] = line[:-1]
            data = b.submit().read()
            r = re.finditer(pattern, data)
            fd.write(line[:-1])
            for i in range(8):
                elem = next(r)
                fd.write(' ' + r.group(1))

fd.close()
