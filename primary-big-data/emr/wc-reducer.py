#!/usr/bin/python 
import sys
import re

def main(argv):
	current_word = None
	current_count = 0
	word = None

	# input comes from STDIN
	for line in sys.stdin:
		# remove leading and trailing whitespace
		line = line.strip()

		# parse the input we got from mapper.py
		word, count = line.split('\t', 1)
		try:
			count = int(count)
		except ValueError:
			continue

		if current_word == word:
			current_count += count
		else:
			if current_word:
				# write result to STDOUT
				print '%s\t%s' % (current_word, current_count)
			current_count = count
			current_word = word

	# the last word
	if current_word == word:
		print '%s\t%s' % (current_word, current_count)

if __name__ == "__main__":
	main(sys.argv)