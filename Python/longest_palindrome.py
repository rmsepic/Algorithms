def check(s: str, left: int, right: int):
	while left >= 0 and right < len(s) and s[left] == s[right]:
		left -= 1
		right += 1

	return right - left - 1

def long_pal(s: str) -> str:
	front = 0
	back = 0

	# Loop through the string
	for i in range(0, len(s)):
		x = check(s, i, i)		# Odd palindrome: "aba"
		y = check(s, i, i + 1) 	# Even palindrome: "baab"
		max_ = max(x, y)

		if max_ > back - front:
			front = i - (max_ - 1) // 2
			back = i + (max_ // 2)

	return s[front:back+1]

def brute_force(s: str) -> str:
	max_len = 1
	start = 0

	# Check all start and end position of each possible palindrome
	for i in range(0, len(s)):
		for j in range(i, len(s)):
			flag = True
			for k in range(0, ((j - i) // 2) + 1):
				if (s[i + k] != s[j - k]):
					flag = False

			if flag == True and (j - i + 1) > max_len:
				max_len = j - i + 1
				start = i

	return s[start:start + max_len]

if __name__ == "__main__":
	s = "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"
	#s = "babac"
	ans = brute_force(s)
	print(ans)
	ans = long_pal(s)
	print(ans)