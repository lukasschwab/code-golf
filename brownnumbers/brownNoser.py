# % Brown numbers have the following properties:
# % 	(m,n) such that:
# % 		n!+1 = m^2
# % Paul Erdos postulated that there are only 3 sets.

# Import the math package
import math
import time

n = 2

# Babylonian method of checking for a square root
# Implement gmpy?

def is_square(apositiveint):
  	x = apositiveint // 2
  	seen = set([x])
  	while x * x != apositiveint:
  	  x = (x + (apositiveint // x)) // 2
  	  if x in seen: return False
  	  seen.add(x)
  	return True

while n > 0: # An intentional infinite loop
	start = time.time()
	m = long(math.factorial(n))+1
	if is_square(m):
		m = math.sqrt(m)
		print '-------------------------' # For legibility
		print 'n = ' + str(n)
		print 'm = ' + str(m)
		end = time.time() # Final time calculation, duplicate for legibility
		print 'Time = ' + str(end-start)
		print '-------------------------' # For legibility
	else:
		print n # Shows how many calculations have been done
		end = time.time() # Final time calculation, duplicate for legibility
		print 'Time = ' + str(end-start)
	n += 1