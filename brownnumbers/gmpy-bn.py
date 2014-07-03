# This is also for the Brown numbers project
# This puts out less data for easier number processing

# % Brown numbers have the following properties:
# % 	(m,n) such that:
# % 		n!+1 = m^2
# % Paul Erdos postulated that there are only 3 sets.

import math
import time
import gmpy
n = 2
while n > 0: # An intentional infinite loop
	start = time.time()
	test = gmpy.fac(n)+1
	if (gmpy.sqrtrem(test))[1]==0:
		m = gmpy.sqrt(test)
		end = time.time() # Final time calculation, duplicate for legibility
		print '-------------------------' # For legibility
		print 'n = ' + str(n)
		print 'm = ' + str(m)
		print 'time = ' + str(end-start)
		print '-------------------------' # For legibility
	else:
		end = time.time() # Final time calculation, duplicate for legibility
		print n
		print end-start
	n += 1