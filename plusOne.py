

def plusOne(digits: list[int]) -> list[int]:

    digits.reverse()
    cary_on = True

    for index in range(len(digits)) : 
        if cary_on : 
            digits[index] += 1
            cary_on = False
                    
        if digits[index] >= 10 : 
            cary_on = True
            digits[index] = 0

    
    if cary_on : 
        digits.append(1)


    digits.reverse()

    return digits
        

print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))
print(plusOne([9,9]))
    