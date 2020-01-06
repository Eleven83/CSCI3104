import math
import random
import numpy as np
import pandas as pd

def cost(S,x,y,i,j):
	indel = 1
	cost = 0
	# if strings are identical, sub cost is zero
	if (x[j-1] == y[i-1]):
		sub = 0
	else:
		sub = 12
	# find optimal cost, include swap if indices within range
	if (i >= 2 and j >= 2):
		cost = min((S[i-1][j-1]+sub),
		(S[i-1][j]+indel),
		(S[i][j-1]+indel))
	else:
		cost = min((S[i-1][j-1]+sub),
		(S[i-1][j]+indel),
		(S[i][j-1]+indel))
	return cost

# x,y are ASCII strings
def alignStrings(x,y):
	nx = len(x)
	ny = len(y)
	
	# initializing matrix
	S = [0]*(ny+1)
	for i in range(ny+1):
		S[i] = [0]*(nx+1)

	# fill in base cases
	for i in range(nx+1):
		S[0][i] = i
	for j in range(ny+1):
		S[j][0] = j
	
	# compute optimal cost through dynammic programming
	for j in range(1,nx+1):
		for i in range(1,ny+1):
			S[i][j] = cost(S,x,y,i,j)
	return S

def determineOptimalOp(S,i,j,x,y):
	# initialize costs
	insert = S[i-1][j]
	delete = S[i][j-1]
	sub = S[i-1][j-1]
	# minVal will contain the possible cost options
	temp = []
	# if possible path, append to minVal
	if (insert+1 == S[i][j]):
		temp.append("insert")
	if (delete+1 == S[i][j]):
		temp.append("delete")
	if (sub+12 == S[i][j]):
		temp.append("sub")
	# include swap if within bounds
	if (i >= 2 and j >= 2):
		swap = S[i-2][j-2]
		if (swap+13 == S[i][j]):
			temp.append("swap")
	# if minVal is empty, then no valid options and 
	# return no_op
	if not temp:
		return "no_op"
	# randomly choose an element from temp
	return random.choice(temp)

def updateIndices(i,j,A):
	# get most recently added optimal operation
	op = A[len(A)-1]
	if op == "insert":
		return (i-1),(j)
	elif op == "delete":
		return (i),(j-1)
	elif op == "no_op" or op == "sub":
		return (i-1),(j-1)
	else:
		return (i-2),(j-2)

# S is an optimal cost matrix from alignStrings
def extractAlignment(S,x,y):
	# empty list of edit operations
	A = []
	# initialize the search for a path to S[0,0]
	[i,j] = [len(y),len(x)]
	while (i > 0 or j > 0):
		# what was an optimal choice?
		A.append(determineOptimalOp(S,i,j,x,y))
		# move to next position
		[i,j] = updateIndices(i,j,A)
	return A

def commonSubstrings(x,L,A):
	A = list(reversed(A))
	subStrings = []
	ss = ""
	n = len(A)
	flag = True	
	for i in range(n):
		# if insert, add a dash to align the string
		if (A[i] == "insert"):
			x = x[:i] + "-" + x[i:]
		# if no_op and flag is true, keep appending 
		# to our current string
		if ((A[i] == "no_op") and (flag == True)):
			ss += x[i]
		# if no_op and flag is false, this is the 
		# beginning of current string
		elif ((A[i] == "no_op") and (flag == False)):
			ss += x[i]
			flag = True
		# if it's not a no_op and flag is true, this
		# is the end of our current string match
		elif ((A[i] != "no_op") and (flag == True)):
			if len(ss) >= L:
				subStrings.append(ss)
			ss = ""
			flag = False
	# edge case for when the string ends with a no_op
	if len(ss) >= L:
		subStrings.append(ss)
	#print(x)
	print(subStrings)

def main():
	# Test 1
	A = []
	x = "APE"
	y = "STEP"
	S = alignStrings(x,y)
	print(S[len(S)-1][len(S[0])-1])
	df = pd.DataFrame(S)
	df.columns = ['-','A','P','E']
	df.index = ['-','S','T','E','P']
	print(df)
	A = extractAlignment(S,x,y)
	print(A)
	commonSubstrings(x,1,A)

	# Test 2
	# x = 'POLYNOMIAL'
	# y = 'EXPONENTIAL'
	# S = alignStrings(x,y)
	# df = pd.DataFrame(S)
	# df.columns = ['-','P','O','L','Y','N','O','M','I','A','L']
	# df.index = ['-','E','X','P','O','N','E','N','T','I','A','L']
	# print(df)
	# A = extractAlignment(S,x,y)
	# commonSubstrings(x,1,A)

	# Part (d) for problem (1a)
    # with open('CS3104/HW/HW5/csci3104_S2018_PS5_data_string_x.txt', encoding='utf8') as myfile:
    #     x = myfile.readline()
    # with open('CS3104/HW/HW5/csci3104_S2018_PS5_data_string_y.txt', encoding='utf8') as myfile2:
    #     y = myfile2.readline()
	# S = alignStrings(x,y)
	# print(S[len(S)-1][len(S[0])-1])
	# A = extractAlignment(S,x,y)
	# commonSubstrings(x,9,A)

if __name__ == '__main__':
	main()