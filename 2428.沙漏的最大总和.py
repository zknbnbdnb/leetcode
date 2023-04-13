#
# @lc app=leetcode.cn id=2428 lang=python3
#
# [2428] 沙漏的最大总和
#

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m - 3):
            for j in range(n - 3):
                tmp = sum(grid[i][j:j + 3]) + sum(grid[i + 1][j:j + 3]) + sum(grid[i + 2][j:j + 3]) - grid[i + 1][j] - grid[i + 1][j + 2]
                res = max(res, tmp)
        return res
# @lc code=end

