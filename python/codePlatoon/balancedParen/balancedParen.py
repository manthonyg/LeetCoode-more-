def balance(str):
    stack = []
    parentheses = []
    mappingRight = {")": "(", "}": "{", "]": "["}
    mappingLeft = {"(": ')', "{": "}", "[": "]"}
    count = 0
    min = 0
    max = 0
    for i,char in enumerate(str):
        if char in mappingLeft:
            count += 1
            parentheses.append(char)
            stack.append(char)
        elif char in mappingRight:
            count -= 1
            top_element = parentheses.pop() if parentheses else '#'
            if count < 0:
                break
            
            elif mappingRight[char] != top_element:
                break
            else:
                stack.append(char)
        else:
            stack.append(char)
    return stack

print(balance("()"))  # should return "()"
print(balance("a(b)c)"))  # should return "a(b)c"
print(balance("(a)(bdd)c)"))  # should return "(a)(bdd)c"
print(balance("a(dbvb)c)"))  # should return "a(dbvb)c"
print(balance("a(b)(c)())"))  # should return "a(b)(c)()"
print(balance(")("))  # should return ""
print(balance("((((("))  # should return ""
print(balance(")(())("))  # should return "(())"
print(balance("(()()("))  # should return "()()"
print(balance(")())(()()("))  # should return "()()()"
