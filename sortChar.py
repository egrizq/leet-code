'''
451. Sort Characters By Frequency

Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 
'''

# todo the logic are to sorted string by max frequencies using counting
def sortCharacters(s:str) -> str:
    temp = {} # create a hash map to store countent string
    2
    # loop through the string
    for i in s:
        # if the string is not in hash map then added if not just add 1
        if i not in temp: 
            temp[i] = 1
        else:
            temp[i] += 1
    
    # sort the hash map by the max of value the create new hash map
    sorting = dict(sorted(temp.items(), key=lambda x:x[1], reverse=True))

    result = [] 
    # loop through the sorted hash map then append the string to the result
    for index, value in sorting.items():
        result.append(value*index) # multiple the string by value, like 'c'*2
        
    return "".join(result) # join all into 1 string

print(sortCharacters("Aabb"))