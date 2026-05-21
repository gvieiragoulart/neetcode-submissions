class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ord_s = "".join(sorted(s))
        ord_t = "".join(sorted(t))

        if ord_s == ord_t:
            return True

        return False
            
            