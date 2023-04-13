#
# @lc app=leetcode.cn id=1626 lang=python3
#
# [1626] 无矛盾的最佳球队
#

# @lc code=start
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        ans = 0
        idx = [i for i in range(n)]
        dp = [0] * n
        idx.sort(key=lambda x: (ages[x], scores[x]))
        for i in range(n):
            tmp = 0
            for j in range(i):
                if scores[idx[i]] >= scores[idx[j]]:
                    tmp = max(tmp, dp[j])
            dp[i] = tmp + scores[idx[i]]
            ans = max(ans, dp[i])
        return ans
# @lc code=end

