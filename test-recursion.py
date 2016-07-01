# Compares time taken for recursive and non-recursive factorial calculation

import time
import sys

sys.setrecursionlimit(1010)

def reF(a):
	if (a == 1):
		return 1
	else:
		return a*reF(a-1)

def oF(a):
	b = a
	while (a>1):
		b = b * (a-1)
		a = a-1
	return b

sys.setrecursionlimit(10001)

tic = time.clock()
reF(10000)
toc = time.clock()
print "Recursive: " + str(toc-tic)

tic = time.clock()
oF(10000)
toc = time.clock()
print "Non-recursive: " + str(toc-tic)