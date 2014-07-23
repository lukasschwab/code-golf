# I want to test the randomness of a random number generator.
# How does randomness increase as you nest pseudorandom number generators?
# I thought no, but wanted to confirm for myself.
# E.g. Randomly selecting from a randomly shuffled list would be two degrees.
# Why use compression? Check this out: https://csclub.uwaterloo.ca/~mtahmed/work_reports/mtahmed_workreport_s12.pdf

# zlib is the python library that does compression.
import zlib
# and this is for randomness!
import random

digitsStr = range(0, 10)

iterations = 0
while iterations <= 100:
  # This generates a random string of numbers.
  uncompressedStr = ""
  while len(uncompressedStr) < 200000:
    repeat = 0
    scrambledDigits = digitsStr
    uncompressedStr += str(scrambledDigits[random.randint(0,9)])

  repeat = 0
  while repeat < iterations:
    random.shuffle(list(uncompressedStr))
    repeat += 1

  uncompressedStr = ''.join(uncompressedStr)

  compressedStr = zlib.compress(uncompressedStr)

  randomness = float(len(compressedStr))/float(len(uncompressedStr))

  print randomness

  iterations = iterations+1
