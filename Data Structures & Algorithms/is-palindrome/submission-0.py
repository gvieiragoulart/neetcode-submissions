class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = len(s) - 1
        right = 0

        while right < left:
            if not s[right].isalnum():
                right += 1
                continue
            elif not s[left].isalnum():
                left -= 1
                continue
            elif s[left].upper() != s[right].upper():
                print("sleft", s[left])
                print("letter", s[right], "right", right)

                return False
            else:
                right += 1
                left -= 1
        
        return True
            
        