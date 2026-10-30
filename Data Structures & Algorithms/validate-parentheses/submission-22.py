class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        seen = []
        pairs = {
        '}':'{',
        ']':'[',
        ')':'('
        }

        for c in s:
            if c not in pairs:
                seen.append(c)
            else:
                if not seen:
                    return False
                if seen.pop() != pairs[c]:
                    return False
        return not seen