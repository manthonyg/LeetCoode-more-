def to_roman(num):
    numerals = ["M", "CM", "D", "CD", "C", "XC",
                "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ''
    i = 0
    while num > 0:
        if num >= values[i]:
            result = result + numerals[i]
            num = num - values[i]
        else:
            i += 1
    return result
