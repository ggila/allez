#!/usr/bin/python

import os
import re

class Latex():

	name = None
	files = None
	tex = None

	def _setIndexMult(self, text):
		with open('index_mult.txt', 'r') as f:
			for line in f:
				l = line[:-1].rsplit('_')
				first = l.pop(0)
				for second in l:
					regex = first + ' ' + second + '([ \.,])'
					print '|' +regex+'|'
					replace = first + ' ' + second + '\\index{' + first.capitalize() + '!' + second + '}\\1'
					text = re.sub(regex, replace, text)
		return text

	def _setIndex(self, text):
		with open('index.txt', 'r') as f:
			for line in f:
				index = '[' + line[0] + line[0].lower() + ']' + line[1:-1] + '([ \.,])'
				regex = index
				replace = line[:-1].lower() + '\\index{' + line[:-1] + '}\\1'
				text = re.sub(index, replace, text)
		return text

	def _setIndexOno(self, text):
		with open('index_onomastique.txt', 'r') as f:
			for line in f:
				index = line[:-1]
				regex = index
				replace = index + '\\index{' + index + '}'
				text = re.sub(index, replace, text)
		return text

	def _setPartTwo(self):
		with open('PartTwo.txt', 'r') as f:
			text = f.read()
			text = self._setIndexOno(text)
#			text = self._setIndexMult(text)
#			text = self._setIndex(text)
			self.tex.write(text)

	def _setPartOne(self):
		with open('PartOne.txt', 'r') as f:
			text = f.read()
			text = self._setIndexOno(text)
#			text = self._setIndexMult(text)
#			text = self._setIndex(text)
			self.tex.write(text)

	def _setCorpus(self):
		self._setPartOne()
		self._setPartTwo()

	def _setAbstract(self):
		with open('abstract.txt', 'r') as f:
			self.tex.write(f.read())

	def _setIntro(self):
		with open('introduction.txt', 'r') as f:
			self.tex.write(f.read())

	def _setThanks(self):
		with open('remerciements.txt', 'r') as f:
			self.tex.write(f.read())

	def make(self):
		str = '\\documentclass[12pt, a4paper]{book}\n\n'
		with open('package.txt', 'r') as f:
			str += f.read()
		str += '\\begin{document}\n\n\\begin{spacing}{1.5}\n\n'
		self.tex.write(str)
		self._setThanks()
		self._setAbstract()
		self._setIntro()
		self._setCorpus()
		str = '\\renewcommand{\\indexname}{Index onomastique}\n'
		str += '\\printindex\n\\end{spacing}\n\\end{document}\n'
		self.tex.write(str)
		self.tex.close()

	def __init__(self, name):
		self.name = name
		self.tex = open(name + '.tex', 'w')

memoire = Latex('poulpe')
memoire.make()
