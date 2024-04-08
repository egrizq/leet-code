/* 
Example 1:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

Example 2:
Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".

Example 3:
Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.
*/

function firstPalindrome(words: string[]): string {
    for (const word of words) {
        let l = 0;
        let r = word.length - 1;

        while (l <= r) {
            if (word[l] !== word[r]) {
                break;
            }
            l++;
            r--;
        }

        if (l >= r) { // If the pointers crossed, it's a palindrome
            return word;
        }
    }
    return ""; // If no palindrome is found
}

console.log(firstPalindrome(["abc", "car", "ada", "racecar", "cool"]));
