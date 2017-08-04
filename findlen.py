
while True:
	word = raw_input("insert word to get word lenght")
	index = 0

	if word == 'done':
		break
	while index < len(word):
		letter = word[index]
		print index,letter
		index = index +1
