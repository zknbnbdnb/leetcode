#
# @lc app=leetcode.cn id=1092 lang=python3
#
# [1092] 最短公共超序列
#

# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        ans = ""
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                ans += str1[i - 1]
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    ans += str1[i - 1]
                    i -= 1
                else:
                    ans += str2[j - 1]
                    j -= 1
        while i > 0:
            ans += str1[i - 1]
            i -= 1
        while j > 0:
            ans += str2[j - 1]
            j -= 1
        return ans[::-1]
# @lc code=end

s = Solution().shortestCommonSupersequence("abac", "cab")