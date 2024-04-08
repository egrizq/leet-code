'''
326. Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:
Input: n = 27
Output: true
Explanation: 27 = 33

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

Example 3:
Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
'''

def isPowerThree(n:int) -> bool:
    if n == 1: return True
    elif n <= 0: return False
    
    temp = n
    while temp != 0:
        status = temp/3
        
        if status == 1:
            return True
        elif status <= 0:
            return False

        temp = status
        
print(isPowerThree(59048))

'''
Solution Bard:

Method 1: Modulo and Division (Faster for 32-bit integers)

Base Cases:

If the number is less than or equal to 0, it cannot be a power of 3, so return False.
If the number is 1, it's the first power of 3, so return True.

Modulo and Division:

Repeatedly divide the number by 3 until it becomes 1 or is no longer divisible by 3.
If at any point during the division, there's a remainder (modulo operation doesn't equal 0), 
the number is not a power of 3, so return False.

Final Check:

If the remaining number after all divisions is 1, the original number is a power of 3, so return True.
'''
