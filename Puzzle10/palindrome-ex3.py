# This producer checks if the string is palindrome
def isPalindrome(str):
	if len(str) == 1 or len(str) == 0:
		print('Palindrome!')
	else:
		if str[0].lower() == str[len(str)-1].lower():
			isPalindrome(str[1:len(str)-1])
		else:
			print('Not palindrome.')

isPalindrome('kaysK')