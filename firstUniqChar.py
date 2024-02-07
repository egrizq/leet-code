'''
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
'''

def firstUniqChar(string):
    temp = {}
    
    for i in string:
        if i not in temp:
            temp[i] = 0
        else:
            temp[i] += 1
    
    for i,v in temp.items():
        if v == 0:
            return string.find(i)
    
    return -1
        
print(firstUniqChar("leetcode"))