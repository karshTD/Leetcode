class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        k = len(s1)


        count_s1 = {}

        for char in s1:
            count_s1[char] = count_s1.get(char, 0) + 1

        count_window= {}

        for i in range(k):
            count_window[s2[i]] = count_window.get(s2[i], 0) + 1
          
            if count_window == count_s1:
                return True

        for i in range(k, len(s2)):
            count_window[s2[i]] = count_window.get(s2[i], 0) + 1

            count_window[s2[i-k]] -= 1

            if count_window[s2[i-k]]==0:
                del count_window[s2[i-k]]
            if count_window == count_s1:
                 return True
        return False