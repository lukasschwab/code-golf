# This is also for the Brown numbers project
# This only outputs the number I care about.

# % Brown numbers have the following properties:
# % 	(m,n) such that:
# % 		n!+1 = m^2
# % Paul Erdos postulated that there are only 3 sets.

import math
import time
import gmpy
n = 1000000000
start = time.time()
test = gmpy.fac(n)+1
if (gmpy.sqrtrem(test))[1]==0:
  m = gmpy.sqrt(test)
  end = time.time() # Final time calculation, duplicate for legibility
  print 'It is a brown number!' # For legibility
  print 'n = ' + str(n)
  print 'm = ' + str(m)
  print 'time = ' + str(end-start)
else:
  end = time.time() # Final time calculation, duplicate for legibility
  print 'Nope.'
  print end-start
