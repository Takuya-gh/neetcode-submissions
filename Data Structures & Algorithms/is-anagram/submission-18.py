class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}

        for c in s:
            if not c in count:
                count[c] = 1
            else:
                count[c] += 1
        
        for c in t:
            if c in count:
                count[c] -= 1
            elif not c in count:
                return False
            if count[c] < 0:
                return False
        return True