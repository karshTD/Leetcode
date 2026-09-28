class Solution:
    def jump(self, nums: list[int]) -> int:
        # If the array has only 1 element, we are already at the end.
        # No jumps needed.
        if len(nums) <= 1:
            return 0
        
        jumps = 0
        current_end = 0      # The furthest index we can reach with our CURRENT number of jumps
        furthest_reach = 0   # The furthest index we can reach if we use ONE MORE jump
        
        # We loop through the array. 
        # Note: We stop at len(nums) - 1 because we don't need to jump FROM the last index.
        for i in range(len(nums) - 1):
            
            # Look at the current square. How far can we reach from here?
            # If it's further than our previous 'furthest_reach', update it.
            furthest_reach = max(furthest_reach, i + nums[i])
            
            # If we have reached the end of our current jump's range...
            if i == current_end:
                # We MUST make a jump now to extend our range.
                jumps += 1
                
                # Our new range extends to the furthest we found.
                current_end = furthest_reach
                
                # If our new range reaches or passes the last index, we are done!
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps