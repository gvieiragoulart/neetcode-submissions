class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table: dict[int, int] = {}

        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1 

            if hash_table[num] > 1:
                return True

        return False



        