class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _hash = {}
        response_list: List[int] = []
        for num in nums:
            _hash[num] = _hash.get(num, 0) + 1

        ordered = sorted(_hash.items(), key=lambda x: x[1], reverse=True)

        return [num for num, count in ordered[:k]]

        