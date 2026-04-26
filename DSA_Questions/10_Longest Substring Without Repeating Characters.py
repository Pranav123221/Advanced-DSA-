objective 10 -> 
Given a string s, find the length of the longest substring without duplicate characters.



## approach:
Approach (Longest Substring Without Repeating Characters)
-> Use sliding window + set/map to track characters in current window
-> Expand window by moving right pointer; if duplicate found, shrink from left until unique
-> Keep updating maximum length of valid window

## constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


## code
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length


## example:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
