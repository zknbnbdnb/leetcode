#
# @lc app=leetcode.cn id=1615 lang=python3
#
# [1615] 最大网络秩
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        cnt = [0] * n
        g = [[0] * n for _ in range(n)]
        for u, v in roads:
            cnt[u] += 1
            cnt[v] += 1
            g[u][v] = 1
            g[v][u] = 1
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                ans = max(ans, cnt[i] + cnt[j] - g[i][j])
        return ans

# @lc code=end

