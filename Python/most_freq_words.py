from typing import List

# 'text' is the text ot be analyzed
# 'exclude' are words that should not be considered
	# Very basic words like 'an' 'a' etc.
def retreiveMostFreqUsedWords(text, exclude):
	words = text.split(" ")	# Split text by " "

	freq = 0
	temp = 0
	ans = []

	# Remove all the excluded words from 'text'
	for e in exclude:
		if (words.count(e) > 0):
			words.remove(e)

	for i in range(0, len(words)):
		words[i] = ''.join(c for c in words[i] if c.isalnum())

	while len(words) != 0:
		word = words.pop(0)
		print(word)
		temp = words.count(word)
		if temp > freq:
			ans = []
			ans.append(word)
			freq = temp
		elif temp == freq:
			ans.append(word)

		# Remove any duplicated after the words have been found
		if words.count(word) > 0:
			for i in range(0, words.count(word)):
				words.remove(word)


	return ans

if __name__ == "__main__":
	text = "We can drink some sodas and listen to some tunes."
	exclude = ["to", "and", "can"]

	ans = retreiveMostFreqUsedWords(text, exclude)
	print(ans)

