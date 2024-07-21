nums = [0,1,2,2,3,0,4,2]
val = 2

index = 0

while True :
    
    if not val in nums : 
        break    

    if nums[index] == val : 
        nums.remove(val) 
        continue

    index += 1 



k = len(nums)

print(nums)
print(k)