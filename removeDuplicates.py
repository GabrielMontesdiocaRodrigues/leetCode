def removeDuplicates(nums : list):
    """
    :type nums: List[int]
    :rtype: int
    """      
    aux = nums.copy()
    unique_numbers = set()
    for num in aux :
        print(num)
        if nums.count(num) >= 2 : 
            nums.remove(num)
            
    print(nums)
    k = len(nums)    
    return k 

print(removeDuplicates([1,1,1,1]))