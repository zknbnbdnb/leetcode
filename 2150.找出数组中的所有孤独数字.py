#
# @lc app=leetcode.cn id=2150 lang=python3
#
# [2150] 找出数组中的所有孤独数字
#

# @lc code=start
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        res = []
        d = Counter(nums)
        for k, v in d.items():
            if v == 1 and k - 1 not in d and k + 1 not in d:
                res.append(k)
        return res
# @lc code=end

