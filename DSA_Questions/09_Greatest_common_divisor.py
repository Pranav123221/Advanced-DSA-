objective 09-> 
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.



  ## approach:
  Approach (GCD – Euclidean Algorithm)
-> Use the relation: GCD(a, b) = GCD(b, a % b)
-> Repeat until b becomes 0
-> The remaining value of a is the GCD


## constraints:
2 <= nums.length <= 1000
1 <= nums[i] <= 1000



## code
class Solution:
    def findGCD(self, nums):
        small = min(nums)
        large = max(nums)
        
        
        while large % small != 0:
            large, small = small, large % small
            
        return small

## example:
Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.
 
