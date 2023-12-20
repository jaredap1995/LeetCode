"""
Given an array of integers heights representing the histogram's bar height where 
the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""



heights = [2,1,5,6,2,3]
heights = [2,4]

class Solution_wrong(object):
    def largestRectangleArea(self, heights):
        stack=[]
        max_area=0
        for idx,height in enumerate(heights):
            while stack and heights[idx]<heights[stack[-1]]:
                top=stack.pop()
                h=heights[top]
                w=idx-top
                area=h*w
                if area>max_area:
                    max_area=area
            stack.append(idx)
        if stack:
            for idx in stack:
                area=heights[idx]*len(heights)-stack[-2]
        return max_area
    

class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)  # Add a guard to handle remaining indices in the stack
        
        for idx, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                top = stack.pop()
                w = idx if not stack else idx - stack[-1] - 1
                max_area = max(max_area, heights[top] * w)
            stack.append(idx)
        
        return max_area

    

print(Solution().largestRectangleArea(heights))