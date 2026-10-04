class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
            min_length = float('inf')
            left = 0
            window_sum = 0

            for right in range(len(nums)):
                window_sum += nums[right]

                while window_sum >= target:
                    min_length = min(min_length, right- left + 1)
                    window_sum -= nums[left]
                    left += 1

            return min_length if min_length != float('inf') else 0