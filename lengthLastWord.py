def lengthOfLastWord(s: str) -> int:
    
    strings = s.strip().split(' ')
    strings.reverse()
    return len(strings[0])


print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))

print("   fly me   to   the moon  ".strip())