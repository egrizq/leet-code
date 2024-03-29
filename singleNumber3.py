'''
260. Single Number III

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]
'''

def singleNumber(nums):
    # return [x for x in nums if nums.count(x) == 1] took a long time
    
    temp = {}
    
    for x in nums:
        if x not in temp:
            temp[x] = 1
        else:
            temp[x] += 1
    
    result = []
    for i, v in temp.items():
        if v == 1:
            result.append(i)        
    return result
    
print(singleNumber([1,2,1,3,2,5]))