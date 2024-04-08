'''
169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

def majorityElement(array):
    temp = {}
    for i in set(array):
        temp[array.count(i)] = i
    return max(temp.items())[1]

print(majorityElement([3,4,3,2,2,2]))