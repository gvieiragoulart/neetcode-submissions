class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count: int = 0
        max_count: int = 0
        last_seen = None

        for i in nums:
            if i == 1:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
            
            last_seen = i
        
        return max_count
        