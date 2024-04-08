/* 
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
*/

function reverseString(s: string[]): string[] {
    
    // init a pointer for left and right of the string
    let l = 0
    let r = s.length-1

    // continue swapping character until the pointers meet/cross
    while(l <= r) {

        // swapping character at current left and right position 
        [s[l], s[r]] = [s[r], s[l]]

        // move the pointers towards the middle string to meet/cross
        l++;
        r--;
    }

    return s
};

console.log(reverseString(["h","e","l","l","o"]))