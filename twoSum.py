def twoSum(nums, target):
    for num in range(len(nums)) : 
        aux = num
        for aux in range(num + 1, len(nums)) : 
            if nums[num] + nums[aux] == target :
                return [num, aux]  
            

         
    