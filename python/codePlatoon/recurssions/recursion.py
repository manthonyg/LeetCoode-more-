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


def roman_num(num):
    answer = ''
    if num == 0:
        return answer
    roman_arabic = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    for key, value in roman_arabic.items():
        if num >= value:
            answer += key
            return answer + roman_num(num - value)

print('start testing roman numeral')
print(roman_num(1) == 'I')
print(roman_num(3) == 'III')
print(roman_num(4) == 'IV')
print(roman_num(964) == 'CMLXIV')
print(roman_num(2437) == 'MMCDXXXVII')

    
        
