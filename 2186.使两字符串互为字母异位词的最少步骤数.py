#
# @lc app=leetcode.cn id=2186 lang=python3
#
# [2186] 使两字符串互为字母异位词的最少步骤数
#

# @lc code=start
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_c = Counter(s)
        t_c = Counter(t)
        res = 0
        for key in s_c:
            if key in t_c:
                res += max(0, abs(s_c[key] - t_c[key])))
            else:
                res += s_c[key]
        for key in t_c:
            if key not in s_c:
                res += t_c[key]
        return res
# @lc code=end

