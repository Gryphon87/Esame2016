#!/usr/bin/python
import sys
def map():
	for line in sys.stdin:
		data = line.strip('\n').split(';')
		year = data[0][:4]
		if (year == "2016"):
			paese = data[2]
			importo = data[6]
			print (paese + '\t' + importo)
						
if __name__ == '__main__':
	map()