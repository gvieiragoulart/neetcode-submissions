class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        right = len(heights) - 1
        left = 0

        while (left < right):
            largura = right - left
            altura = min(heights[right], heights[left])

            result = altura * largura

            if result > max_water:
                max_water = result
    
            if heights[left] < heights[right]:
                left += 1
                continue
            
            right -= 1


        return max_water
                
        