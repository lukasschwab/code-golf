import random
ASCII = [chr(x) for x in range(128)]

def gen_markov(text):
	out = {}
	for i in range(0, len(text)-1):
		x, y = text[i], text[i+1]
		if x in ASCII and y in ASCII:
			if x in out and y in out[x]:
				out[x][y] += 1
			elif x in out:
				out[x][y] = 1
			else:
				out[x] = {y: 1}
	for char in ASCII:
		if char not in out:
			out[char] = {}
			for char2 in ASCII:
				out[char][char2] = 1
	return out

def pick_letter(markov, state):
	state_weights = markov[state]
	choices_list = []
	for char in state_weights:
		choices_list += [char] * state_weights[char]
	return random.choice(choices_list)


def make_phrase(markov, len):
	char = random.choice(ASCII)
	out = char
	for i in range(0, len):
		char = pick_letter(markov, char)
		out += char
	return out