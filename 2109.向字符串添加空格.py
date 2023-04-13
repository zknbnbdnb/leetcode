#
# @lc app=leetcode.cn id=2109 lang=python3
#
# [2109] 向字符串添加空格
#

# @lc code=start
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        cur = 0
        t = []
        for i in spaces:
            a.append(s[cur:i])
            cur = i
        t.append(s[cur:])
        return ' '.join(t)
        # @lc code=end

