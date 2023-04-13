#
# @lc app=leetcode.cn id=1039 lang=python3
#
# [1039] 多边形三角剖分的最低得分
#

# @lc code=start
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i + 1 == j:
                return 0
            res = float('inf')
            for k in range(i + 1, j):
                res = min(res, dfs(i, k) + dfs(k, j) + values[i] * values[k] * values[j])
            return res
        return dfs(0, len(values) - 1)

s = Solution().minScoreTriangulation([1,3,1,4,1,5])
print(s)
# @lc code=end

