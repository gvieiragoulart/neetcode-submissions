class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            b = i + 1
            c = len(nums) - 1

            while (b < c):
                result = a + nums[b] + nums[c]
                if result > 0:
                    c -= 1
                elif result < 0:
                    b += 1
                else:
                    results.append([a, nums[b], nums[c]])
                    b += 1
                    while nums[b] == nums[b - 1] and b < c:
                        b += 1

        return results




        