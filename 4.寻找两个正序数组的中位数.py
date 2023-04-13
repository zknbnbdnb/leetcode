#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        leng = len(nums1)
        if leng % 2:
            return float(nums1[leng//2])
        else:
            return (nums1[leng // 2] + nums1[leng // 2 - 1]) / 2

# @lc code=end
