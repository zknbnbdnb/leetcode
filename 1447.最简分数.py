#
# @lc app=leetcode.cn id=1447 lang=python3
#
# [1447] 最简分数
#

# @lc code=start
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [f"{i}/{j}" for i in range(1, n) for j in range(i + 1, n + 1) if math.gcd(i, j) == 1]
# @lc code=end

