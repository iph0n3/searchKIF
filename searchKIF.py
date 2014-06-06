#coding: utf-8
#date: 2014/02/12

import os
import sys

def search(keyword):
	path  = os.getcwd()
	files = os.listdir(path)
	
	for file in files:
		if os.path.isfile(file):
			f = open(file, 'r')
			content = f.readlines()
			for i in content:
				if keyword in i:
					print '[+] %s in %s'%(keyword, file)
					print '[-] line: %d'%content.index(i)
		else:
			pass
def run():
	search(sys.argv[1])

if __name__ == '__main__':
	run()