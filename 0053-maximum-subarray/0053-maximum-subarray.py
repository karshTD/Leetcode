class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = 0
        max_sum = nums[0]

        for num in nums:
            if current_sum < 0:
                current_sum = num
            else:
                current_sum = current_sum + num

            if current_sum > max_sum:
                max_sum = current_sum

       
        return max_sum
    
            