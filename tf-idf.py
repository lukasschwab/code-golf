# An implementation of the tf-idf word importance algorithm

from __future__ import division, unicode_literals
import math
from textblob import TextBlob as tb

def tf(word, blob):
	return blob.split(' ').count(word) / len(blob.split(' '))

def n_containing(word, bloblist):
	return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
	return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def printout(bloblist, top=3):
	for i, blob in enumerate(bloblist):
		print("Top words in document {}".format(i + 1))
		scores = {word: tfidf(word, blob, bloblist) for word in blob.split(' ')}
		sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
		for word, score in sorted_words[:top-1]:
			print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))