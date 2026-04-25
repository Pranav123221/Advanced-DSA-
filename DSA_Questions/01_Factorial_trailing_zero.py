# 01 problem:
Given an integer n, return the number of trailing zeroes in n!.

# Approach 
-> Given an integer n, return the number of trailing zeroes in n!.

->Keep dividing n by 5, 25, 125… and add the results

->The total sum gives the number of trailing zeroes in n!

#constraints
- Constraints:

0 <= n <= 104


# code in python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        
        while n > 0:
            n //= 5
            count += n
            
        return count

# example:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.


  #output
  


  
  


