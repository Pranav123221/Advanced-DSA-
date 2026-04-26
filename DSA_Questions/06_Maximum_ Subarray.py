objective 06 -> Given an integer array nums, find the subarray with the largest sum, and return its sum.


## Approach ->
  Approach (Maximum Subarray – Kadane’s Algorithm)
-> Traverse the array and keep a running sum (current sum)
-> If current sum becomes negative, reset it to 0
-> Keep updating maximum sum encountered during traversal


## constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104


## code
class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum


## example:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
