import mechanize
import re

url = 'https://duoquadragintien.fr'

fd=open('hours.txt', 'w')

pattern = re.compile('<a class="project-item block-item"[^-]+-([^-]+)-d06">[^\n]+\n(<[^\n]+\n){3}<span[^>]+>in progress')

b = mechanize.Browser()
b.open(url)
b.select_form(nr=0)
b['user[login]']='ggilaber'
b['user[password]']='Valpara1s0'
b.submit()

with open('./student.txt', 'r') as f:
    for line in f:
        fd = b.open(url2 + line)
        r = re.finditer(pattern, fd.read())
        print line[:-1]
        if not r: fd_no.write(line)
        else:
            for elem in r:
                print elem.group(1)
                write_in_txt(elem.group(1), line)
