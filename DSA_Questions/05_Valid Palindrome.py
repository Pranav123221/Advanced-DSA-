objective 05 -> 
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

## Approach->
-> Use two pointers: one at start and one at end of string
-> Ignore non-alphanumeric characters and compare lowercase characters
-> If all matching → palindrome, else not


## constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.


## code
                               class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()
        
        return cleaned == cleaned[::-1]




## example:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
