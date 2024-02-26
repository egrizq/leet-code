'''
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

k = the length of most frequent elements/ array 

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''

def topKFrequent(nums, k):

    temp = []
    for x in set(nums):
        temp.append([x, nums.count(x)])
        
    new = sorted(temp, key=lambda x: (x[1], x[0]))[::-1]
    
    result = []
    for x in new:
        if len(result) < k:
            result.append(x[0])
    return result
    
print(topKFrequent([1,1,1,2,2,3], 2))
