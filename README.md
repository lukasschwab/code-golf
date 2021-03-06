code-golf
=========

StackExchange Code Golf and little snippets of code. All for fun.

Update June 30, 2016: I think I will use this more for one-off scripts that I do not think will be generally useful... but you never know :)

I'll try to keep a description of what is what organized here, but most of this is code written on impulse very late at night.

+ `/brownnumbers`
    + brownNoser.py implements the Babylonian method of finding a perfect square to isolate brown numbers
    + bab-timer.py times the Babylonian method of finding a perfect square for runtime analysis // complexity approximation
+ `/golf`
	+ big-number.py tries to print a very large number with very few characters.
	+ flipped-number.m flips a number upside down.
	+ matrix-compare.m compares two matrices.
	+ rotate.m rotates a matrix. Easy.
+ `/trell` is a dead simple Chrome extension that modifies Trello's CSS (works as of July 14, 2017; probably won't for long)
+ `test-recursion.py` tests time taken for recursive and non-recursive factorial calculations.
+ `tf-idf.py` is a rudimentary implementation of tf-idf.
+ `tictactoe.py` is an attempted CLI for tic tac toe.
+ `recursive.py` is a meta-recursive Python script. Rather than recursively calling a function, it infinitely recursively starts a new Python process runnint itself. Spooooky.
+ `markov.py` does something with letters and a markov chain. I think it generates fake words.
+ `randomness-test.py` determines the degree of randomness of python's pseudorandom number generator by comparing a random string to a compressed random string, to prove to myself that randomness doesn't increase with iteration.
+ `sports-scraper.py` scrapes sportslogos.net for sports teams logos, part of work I did with Simar Mangat @ Pavlov.
+ `readme.sh` generates my standard README template so I don't have to copy it by hand.
+ `md-to-pdf.sh` uses [pandoc](http://pandoc.org/) to apply some hacky preprocessing to a markdown document before converting it to PDF with LaTeX.
+ `codecat.sh` renders Python code into a PDF, which is appended to another PDF. This is useful for [EE 16A homework](http://inst.eecs.berkeley.edu/~ee16a/sp18/).
+ `glookup.exp` is an expect script to check course grades on UC Berkeley EECS machines. Unlikely to be broadly useful.
