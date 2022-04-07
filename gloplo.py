# ʔ

import sys
#import math

# open file
src = open( sys.argv[1], "r" )

funDef = False
funLine = 0
currFun = ""

# types
types = ["Int", "Arr"]
# store function definistion
functions = {}
# variables memory
variables = {}

# lexer function
def lexer( src ):
	global functions
	global funDef
	global funLine
	global types
	
	for line in src:
		# remove \n from lines except last
		if line[-1] == "\n":
			line = line[0:-1]
		
		tokens = line.split(" ")
		if funDef:
			if line[0] == "\t":
				currFunDef = functions.get( currFun )
				currFunDef.append( line )
				functions.update({ currFun: currFunDef })
				funLine += 1
			else:
				funDef = False
				currFun = ""
				funLine = 0
		elif tokens[0] == "funct":
			funDef = True
			currFun = tokens[2]
			functions.update({ currFun: [] })
		elif tokens[0] in types:
			namespace = tokens[1]
			value = " ".join( tokens[3:] )
			# value = parseExp( value )
			variables.update({ namespace: value })

lexer(src)
print( variables )
print( functions )