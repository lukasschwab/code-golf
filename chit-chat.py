import cleverbot
import time

cb1 = cleverbot.Cleverbot()
cb2 = cleverbot.Cleverbot()

x = 1

print '2: Hi. How are you?'
test = cb1.ask('Hi. How are you?')

while x > 0:
	print "1: " + test
	time.sleep(3)
	test2 = cb2.ask(test)
	print "2: " + test2
	time.sleep(3)
	test = cb1.ask(test2)