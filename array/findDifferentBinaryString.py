'''
1980. Find Unique Binary String
Given an array of strings nums containing n unique binary strings each of length n, 
return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
'''

def findDifferentBinaryString(nums):
    for num in nums:
        if num[::-1] not in nums:
            return num[::-1]
        
        n = 1
        for char in num:
            newChar0 = num.replace("0", "1", n)
            if newChar0 not in nums:
                return newChar0
            
            newChar1 = num.replace("1", "0", n)
            if newChar1 not in nums:
                return newChar1
            
            n += 1
    
print(findDifferentBinaryString(["0"]))