'''
1941. Check if all characters have equal number of Occurences

Given a string s, return true if s is a good string, or false otherwise.
A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

Example 1:
Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

Example 2:
Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
'''

def areOccurrencesEqual(s):
    temp = {}
    for char in s:
        if char not in temp:
            temp[char] = 1
        else:
            temp[char] += 1
    
    return len(set(temp.values())) == 1

print(areOccurrencesEqual("aaabb"))