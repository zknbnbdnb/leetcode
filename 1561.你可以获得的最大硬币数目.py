#
# @lc app=leetcode.cn id=1561 lang=python3
#
# [1561] 你可以获得的最大硬币数目
#

# @lc code=start
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        return sum(piles[-2 * i - 2] for i in range(n))

        # @lc code=end
