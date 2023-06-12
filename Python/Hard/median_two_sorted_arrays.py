"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


"""

nums1=[2,20]
nums2=[1,3,4,5,6]

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1

        n1=len(nums1)
        n2=len(nums2)

        left=0
        right=n1

        while left<=right:
            mid1=(left+right)//2
            mid2=(n1+n2+1)//2-mid1

            maxLeft1=nums1[mid1-1] if mid1 !=0 else float('-inf')
            minRight1=nums1[mid1] if mid1!= n1 else float('inf')

            maxLeft2 = nums2[mid2-1] if mid2 != 0 else float('-inf')
            minRight2 = nums2[mid2] if mid2 != n2 else float('inf')

            if maxLeft1<=minRight2 and maxLeft2 <= minRight1:
                if (n1+n2)%2==0:
                    return float(max(maxLeft1, maxLeft2)+min(minRight1, minRight2))/2
                else:
                    return float(max(maxLeft1, maxLeft2))
            elif maxLeft1>minRight2:
                right=mid1-1
            else:
                left=mid1+1

        return -1

print(Solution().findMedianSortedArrays(nums1, nums2))

