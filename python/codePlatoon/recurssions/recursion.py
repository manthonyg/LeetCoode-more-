import re
def palindrome(string):
	converted = re.sub('[\W_]+', '', str(string).lower())
	length_word = len(converted)
	if len(converted) == 1 or len(converted) == 0:
		return True
	if converted[0] == converted[-1]:
		# move left and right pointer inward one letter
		# left: 0
		# right: -1 => last index
		# left => 1
		# right => -2 == second last index
		return palindrome(converted[1:-1])
	else:
		return False


print('start palindrome test.........')
print(palindrome('racecar') == True)
print(palindrome('Noon') == True)
print(palindrome('ciVic') == True)
print(palindrome('nice') == False)
print(palindrome(434) == True)
print(palindrome(123) == False)
print(palindrome('bomb') == False)
print(palindrome('SorewasIereIsawEros.') == True)
print(palindrome('A man, a plan, a canal -- Panama') == True)
