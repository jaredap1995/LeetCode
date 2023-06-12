"""Given n non-negative integers representing an elevation map 
where the width of each bar is 1, 
compute how much water it can trap after raining.


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented 
by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
"""

height=[0,1,0,2,1,0,1,3,2,1,2,1]

class Solution:
    def trap(self, height):
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
    

"""The key idea in this problem is that at any index the amount of water trapped 
depends on the height of the bars on the left and right side (similar to the container with the most water problem).
But we do not know the max heights of the bars while traversing the array.

We use two pointers to check the max height on left and right side and update the left and 
right heights accordingly. We only increment on the left or right when the left/right is 
the smaller/shorter side. 

At each step we update our max height when a new max is encountered and when a height on right or left is encountered
that is less than the ,max of taht correspodning side, we know water can be trapped, so 
we subtract the (max height for that side) - the current height and keep on incrementing."""
