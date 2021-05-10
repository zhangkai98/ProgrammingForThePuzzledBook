str1 = 'BWWWWWBWWWW'
str2 = 'AAAAAAABBNNNNNNMMMWWWWWW'
str3 = ''

def rlcompress(string):
	string = string + str(0)
	start = 0
	res = ''
	for i in range(1, len(string)):
		if string[i] != string[i-1]:
			res = res + str(i-start) + string[start]
			start = i
	print(res)

## rlcompress(str1)
## rlcompress(str2)
rlcompress(str3)

compressed_str1 = '3B5W7B11W'
compressed_str2 = ''

def rldecompress(string):
	start = 0
	res = ''
	for i in range(1, len(string)):
		if string[i].isalpha():
			for j in range(int(string[start:i])):
				res = res + string[i]
			start = i + 1
	print(res)

rldecompress(compressed_str2)