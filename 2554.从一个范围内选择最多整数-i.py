#
# @lc app=leetcode.cn id=2554 lang=python3
#
# [2554] 从一个范围内选择最多整数 I
#

# @lc code=start
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        db = [1] * (n + 1)
        for i in banned:
            if i <= n:
                db[i] = 0
        ans, sum_ = 0, 0
        for i in range(1, n + 1):
            if db[i]:
                sum_ += i
                if sum_ <= maxSum:
                    ans += 1
                else:
                    break
        return ans
# @lc code=end

