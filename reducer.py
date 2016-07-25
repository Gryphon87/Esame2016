#!/usr/bin/python
import sys

def reduce():
	#support variables
	current = -99
	cimporto = 0
	for pipe in sys.stdin:
		line = pipe.strip('\n').split('\t')
		paese = line[0]
		importo = int(line[1])

		# the first iteration will override the current var
		if (current == -99):
			current = paese

		# if the var doesn't change it will add the value
		if (paese == current):
			cimporto += importo
		else:
			#print the previous values and reset the current ones
			print ('paese ' + str(current) + ': ' + str(cimporto))
			current = paese
			cimporto = importo

	#print the last value
	print ('paese ' + str(current) + ': ' + str(cimporto))

if __name__ == '__main__':
	reduce()