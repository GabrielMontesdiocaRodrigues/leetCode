def romanToInt(s):
    def buildRomanNum(*romanNums): 
        def romanNumber(value, nextRomanNumber) :
            realValue = 0 
            for romanNum in romanNums : 
                if (romanNum ==  nextRomanNumber or romanNum == nextRomanNumber) and value == 1 : 
                    realValue = -1
                    break
                if (romanNum ==  nextRomanNumber or romanNum == nextRomanNumber) and value == 10 : 
                    realValue = -10
                    break
                if (romanNum ==  nextRomanNumber or romanNum == nextRomanNumber) and value == 100 : 
                    realValue = -100
                    break
            if realValue == 0 : 
                return value
            return realValue
        return romanNumber

    realValue_I = buildRomanNum('X','V')
    realValue_X = buildRomanNum('L','C')
    realValue_C = buildRomanNum('D','M')

    result = 0  
    nextRomanNum = ''  
    for iter in range(len(s)):
        romanNum = s[iter]
        if iter + 1 < len(s) : 
            nextRomanNum = s[iter+1]
        if romanNum == 'I' : 
            result += realValue_I(1, nextRomanNum) 
            continue
        if romanNum == 'V' : 
            result += 5 
            continue
        if romanNum == 'X' : 
            result += realValue_X(10, nextRomanNum)
            continue
        if romanNum == 'L' : 
            result += 50 
            continue
        if romanNum == 'C' : 
            result += realValue_C(100, nextRomanNum)
            continue
        if romanNum == 'D' : 
            result += 500 
            continue
        if romanNum == 'M' : 
            result += 1000 
            continue
    return result

