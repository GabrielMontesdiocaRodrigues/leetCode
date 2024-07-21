def isValid(s: str) -> bool:

    openers = ('(', '[', '{')
    closers = (')', ']', '}')

    opens = []

    for char in s:
        if not opens and char in closers:
            valid = False
            break

        if char in openers:
            valid = False
            opens.append(char)
            continue

        opener = openers[closers.index(char)]

        if char in closers and opener in opens:
            valid = True
            opens.remove(opener)
            continue

    if opens:
        valid = False

    return valid


print(isValid("()"))  # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False
print(isValid("[]"))  # True
print(isValid("([)]"))  # False
print(isValid("({[)"))  # False
print(isValid("{[]}"))  # True
