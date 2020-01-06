import math,random
import numpy as np
import pandas as pd 


# Helper functions
def determineOptimalOp(S,i,j,x,y):
	insert = S[i-1][j]
	delete = S[i][j-1]
	sub = S[i-1][j-1]
	M = []
	if (insert+1 == S[i][j]):
		M.append("insert")
	if (delete+1 == S[i][j]):
		M.append("delete")
	if (sub+2 == S[i][j]):
		M.append("sub")
	if not M:
		return "no_op"
	# Uniformly random choice
	return random.choice(M)

def updateIndices(S,i,j,a):
	operation = a[len(a)-1]
	if operation == "insert":
		return (i-1),(j)
	elif operation == "delete":
		return (i),(j-1)
	elif operation == "no_op" or operation == "sub":
		return (i-1),(j-1)

# Cost function
def cost(S,x,y,i,j):
	# operation costs
	cost = 0
	indel = 1	
	# cost of sub is 2, except when x(i) = y(j), which is a “no-op” and has cost 0.
	if (x[j-1] == y[i-1]):
		sub = 0
	else:
		sub = 2
	# Only three options to find cost (swap not used here)
	if (i >= 2 and j >= 2):
		cost = min((S[i-1][j-1]+sub),
		(S[i-1][j]+indel),
		(S[i][j-1]+indel))
	else:
		cost = min((S[i-1][j-1]+sub),
		(S[i-1][j]+indel),
		(S[i][j-1]+indel))

	return cost

# takes as input two ASCII strings x and y
def alignStrings(x,y):
	nx = len(x)
	ny = len(y)
	
	# Initialize S, table of length nx by ny for memoizing the subproblem costs
	S = [0]*(ny+1)
	for i in range(ny+1):
		S[i] = [0]*(nx+1)

	# Base cases: first column and first row
	for i in range(nx+1):
		S[0][i] = i
	for j in range(ny+1):
		S[j][0] = j
	# Optimal cost for x[0..i] and y[0..j]
	for j in range(1,nx+1):
		for i in range(1,ny+1):
			S[i][j] = cost(S,x,y,i,j)
	return S

# S is an optimal cost matrix from alignStrings
def extractAlignment(S,x,y):
	# Initialize a, an empty list of edit operations
	a = []
	# Initialize the search for a path to S[0,0]
	[i,j] = [len(y),len(x)]

	while (i > 0 or j > 0):
		# what was an optimal choice?
		a.append(determineOptimalOp(S,i,j,x,y))
		# move to next position
		[i,j] = updateIndices(S,i,j,a)
	return a

#def commonSubstrings(x,L,a):
	# returns each of the substrings of length at least L in x that aligns exactly, via a run of no-ops, to a substring in y

def main():
	#a = []

	x = "APE"
	y = "STEP"
	S = alignStrings(x,y)

	x = 'POLYNOMIAL'
	y = 'EXPONENTIAL'
	S = alignStrings(x,y)

	with open('CS3104/HW/HW5/csci3104_S2018_PS5_data_string_x.txt', encoding='utf8') as myfile:
		x = myfile.readline()
	with open('CS3104/HW/HW5/csci3104_S2018_PS5_data_string_y.txt', encoding='utf8') as myfile2:
		y = myfile2.readline()
	S = alignStrings(x,y)
	a = extractAlignment(S,x,y)
	#commonSubstrings(x,20,a)

if __name__ == '__main__':
	main()