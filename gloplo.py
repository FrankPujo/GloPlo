# ʔ

import sys
#import math

# open file
src = open( sys.argv[1], "r" )

funDef = False
funLine = 0
currFun = ""

# store function definistion
functions = {}

# lexer function
def lexer( src ):
	global functions
	global funDef
	global funLine
	
	for line in src:
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

lexer(src)
print( functions )