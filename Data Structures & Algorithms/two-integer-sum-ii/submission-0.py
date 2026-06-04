class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        alto = len(numbers) - 1
        baixo = 0


        left = baixo
        right = alto

        while (left < right):
            soma = numbers[left] + numbers[right]

            if soma == target:
                return [left + 1, right + 1]
            elif soma < target:
                left += 1
            else:
                right -= 1