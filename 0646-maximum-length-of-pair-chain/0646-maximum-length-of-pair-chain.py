class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])
        count = 0
        last = float('-inf')
        for a, b in pairs:
            if a > last:
                count += 1
                last = b
        return count