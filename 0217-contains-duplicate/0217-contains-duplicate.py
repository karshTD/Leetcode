class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        if not  nums:
            return False
        
        if len(nums)==1:
            return False

        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
