def solution(nums1, nums2):
    i = sorted(list(set(nums1).intersection(set(nums2))))
    if i: return i[0]
    else: return -1