#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        a = len(ratings)
        result = [1 for i in range(a)]
        for i in range(a-1):
            if ratings[i+1] > ratings[i]:
                result[i+1] = + result[i] + 1
        for i in range(a-1, -1, -1):
            if ratings[i] < ratings[i-1] and i > 0:
                result[i-1] = max(result[i] + 1, result[i-1])  # 防止多加一
        return sum(result)
        # @lc code=end
