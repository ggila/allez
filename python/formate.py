#!/usr/bin/python

import sys
from os import listdir
import re

def formate(dirname):
	regex = r'(>[^\n]+\n[^\n]+)\n([^>])'
	replace = r'\1\2'
	for file in listdir(dirname):
		f = open(dirname + '/' + file, 'r')
		text = f.read()
		f.close()
		f = open(dirname + '/' + file, 'w')
		while re.search(regex, text):
			text = re.sub(regex, replace, text)
		text = text.upper()
		f.write(text)
		f.close()
