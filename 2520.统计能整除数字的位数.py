#
# @lc app=leetcode.cn id=2520 lang=python3
#
# [2520] 统计能整除数字的位数
#

# @lc code=start
class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        arr = [int(i) for i in str(num)]
        for i in arr:
            if i != 0 and num % i == 0:
                res += 1
        return res
# @lc code=end

