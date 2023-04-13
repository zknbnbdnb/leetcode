#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        return int('{0:032b}'.format(n)[::-1], 2)
# @lc code=end


s = Solution()
print(s.reverseBits(43261596))
