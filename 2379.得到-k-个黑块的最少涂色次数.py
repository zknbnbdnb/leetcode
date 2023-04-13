#
# @lc app=leetcode.cn id=2379 lang=python3
#
# [2379] 得到 K 个黑块的最少涂色次数
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i, j = 0, k - 1
        n = len(blocks)
        res = []
        while j < n:
            res.append(blocks[i:j + 1].count('W'))
            i += 1
            j += 1
        return min(res)
# @lc code=end

