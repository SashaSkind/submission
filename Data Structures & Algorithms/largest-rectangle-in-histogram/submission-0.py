class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        start_i = 0
        for i, h in enumerate(heights):
            start_i = i

            while stack and h < stack[-1][1]:
                prev_i, prev_h = stack.pop()
                start_i = prev_i
                area = prev_h * (i - prev_i)
                max_area = max(area, max_area)
                
            if len(stack) == 0 or h >= stack[-1][1]:
                stack.append((start_i, h))

        for start_i, h in stack:
            max_area = max(max_area, h * (len(heights) - start_i))
            
        return max_area




        