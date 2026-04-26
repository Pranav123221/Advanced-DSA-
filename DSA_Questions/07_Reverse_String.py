objective 07 ->
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



## Approach->
  Approach (Reverse String)
-> Use two pointers: one at start and one at end
-> Swap characters at both positions
-> Move pointers inward until they meet


## constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.



## code

  class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


## example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]


  
