#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start


class Solution:
    def countBits(self, n: int):
        res = [0 for _ in range(n + 1)]
        for i in range(n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res
        # @lc code=end


s = Solution()
print(s.countBits(13))
