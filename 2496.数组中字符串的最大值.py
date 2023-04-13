#
# @lc app=leetcode.cn id=2496 lang=python3
#
# [2496] 数组中字符串的最大值
#

# @lc code=start
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = []
        for s in strs:
            if s.isdigit():
                res.append(int(s))
            else:
                res.append(len(s))
        return max(res)
# @lc code=end

