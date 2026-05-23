class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _hash_strs: dict[str, list[int]] = {}

        for i, s in enumerate(strs):
            sorted_string =  "".join(sorted(s))
            if sorted_string in _hash_strs:
                _hash_strs[sorted_string].append(s)
            else:
                _hash_strs[sorted_string] = []
                _hash_strs[sorted_string].append(s)
        
        response: List[List[str]] = []
        for hash_str in _hash_strs:
            response.append(_hash_strs[hash_str])

        return response

        