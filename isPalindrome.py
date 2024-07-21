def isPalindrome(x):
    stringIn = str(x)
    stringInReverse = ''
    for letter in range(len(stringIn),0,-1) :
        stringInReverse += stringIn[letter-1] 
    if  stringIn == stringInReverse :
        return True
    return False
    