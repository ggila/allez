import mechanize
import re

url = 'https://intrav2.42.fr'
url2 = 'https://profile.intrav2.42.fr/users/'

fd_php=open('php.txt', 'w')
fd_cpp=open('cpp.txt', 'w')
fd_ocaml=open('ocaml.txt', 'w')
fd_unity=open('unity.txt', 'w')
fd_no=open('no.txt', 'w')

def write_in_txt(piscine, line):
    if piscine == 'php': fd_php.write(line)
    elif piscine == 'cpp': fd_cpp.write(line)
    elif piscine == 'ocaml': fd_ocaml.write(line)
    elif piscine == 'unity': fd_unity.write(line)

pattern = re.compile('<a class="project-item block-item"[^-]+-([^-]+)-d06">[^\n]+\n(<[^\n]+\n){3}<span[^>]+>in progress')

b = mechanize.Browser()
b.open(url)
b.select_form(nr=0)
b['user[login]']='ggilaber'
b['user[password]']=
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
