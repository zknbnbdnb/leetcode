#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        i, j, res = n // 7, n % 7, 0
        temp = i
        for k in range(i + 1, i + j + 1):
            res += k
        while temp:
            res += 28 + 7 * (temp - 1)
            temp -= 1
        return res


# @lc code=end
a = Solution()
print(a.totalMoney(30))
