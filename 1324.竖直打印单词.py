#
# @lc app=leetcode.cn id=1324 lang=python3
#
# [1324] 竖直打印单词
#

# @lc code=start
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(map(len, words))
        res = []
        for i in range(max_len):
            res.append(''.join([w[i] if i < len(w) else ' ' for w in words]).rstrip())
        return res
# @lc code=end

