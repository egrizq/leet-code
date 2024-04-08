def findFinalValue(nums, original):
    start = 0
    end = len(nums)-1
    
    temp = original
    while start<=end:
        if temp in nums:
            temp = original*2
            start = 0
        elif temp not in nums:
            start += 1
    
    return temp
    
    
print(findFinalValue([5,3,6,1,12], 3))