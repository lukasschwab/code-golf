# Lukas Schwab 6/18/14

# http://codegolf.stackexchange.com/questions/31695/largest-number-in-ten-bytes-of-code

# --------------------

# Here's a solution with too many characters.
# Also, it relies on x having a value beforehand.
# Note that "print x" can be excluded from the character count.
# However, it will print an inifinitely large number if given enough time.
# Is there a simpler while loop in some language?

while x>0
	x+=9
	print x

# 15 characters