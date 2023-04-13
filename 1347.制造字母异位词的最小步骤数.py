#
# @lc app=leetcode.cn id=1347 lang=python3
#
# [1347] 制造字母异位词的最小步骤数
#

# @lc code=start
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ds, dt = Counter(s), Counter(t)
        res = 0
        for k, v in ds.items():
            if k in dt:
                res += max(0, v - dt[k])
            else:
                res += v
        return res
# @lc code=end

