#
# @lc app=leetcode.cn id=2570 lang=python3
#
# [2570] 合并两个二维数组 - 求和法
#

# @lc code=start
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d_1, d_2 = {}, {}
        for i, v in nums1:
            d_1[i] = v
        for i, v in nums2:
            d_2[i] = v
        for k, v in d_2.items():
            if k in d_1:
                d_1[k] += v
            else:
                d_1[k] = v
        return sorted(d_1.items(), key=lambda x: x[0])

# @lc code=end

