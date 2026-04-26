objective 03 -> Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.



##approach ->
Approach (Valid Parentheses)
-> Use a stack to keep track of opening brackets
 ->For every closing bracket, check if it matches the top of the stack
 -> If stack is empty at end → valid, otherwise invalid



## constraints
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.



## code

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for ch in s:
            if ch in mapping.values():   # opening bracket
                stack.append(ch)
            else:   # closing bracket
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
        
        return len(stack) == 0


## example:
Input: s = "()"

Output: true
  
