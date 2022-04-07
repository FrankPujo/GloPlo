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

# utils
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ints = "0123456789"

# find function evaluation
def evalFun( funName, arg ):
	global functions
	global types
	global variables
	global alpha
	
	fValue = None
	# evaluate function when called
	funDef = functions.get( funName )
	for defin in funDef:
		toks = defin.split(" ")
		case = toks[0]
		rawVal = toks[2:]
		newVal = []
		for lVal in rawVal:
			if lVal[0] in alpha:
				lVal = str(variables.get( arg ))
			newVal.append( lVal )
		value = eval( " ".join( v for v in newVal ) )
		if case == "_":
			fValue = value
			break
		elif str(variables.get(arg)) == str(case):
			fValue = value
			break
	return fValue


# parse variable definition
def parseExp( expression ):
	global functions
	
	toks = expression.split(" ")
	print( toks[0] )
	if toks[0] in functions:
		value = evalFun( toks[0], toks[1] )
	else:
		value = eval( expression )
	parsed = value
	return parsed

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
			if line == "":
				funDef = False
				currFun = ""
				funLine = 0
			elif line[0] == "\t":
				line = line[1:]
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
			currFun = tokens[1]
			functions.update({ currFun: [] })
		elif tokens[0] in types:
			namespace = tokens[1]
			rawVal = " ".join( tokens[3:] )
			value = parseExp( rawVal )
			variables.update({ namespace: value })
		elif line[:6] == "output":
			outp = line[7:]
			print( outp )

lexer(src)
print( variables )
print( functions )