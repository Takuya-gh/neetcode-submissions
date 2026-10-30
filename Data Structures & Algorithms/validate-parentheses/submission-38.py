class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []

        pairs = {
            '}':'{',
            ']':'[',
            ')':'('
        }
    
        for b in s:
            if b not in pairs:
                stack.append(b)
            else:
                if not stack:
                    return False
                if stack.pop() != pairs[b]:
                    return False
        return True if not stack else False

