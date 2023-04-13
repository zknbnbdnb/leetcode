
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high, cur = 1, n, 0
        while low <= high:
            mid = (low + high) // 2
            if not isBadVersion(mid):
                cur = mid
                low = mid + 1
            else:
                high = mid - 1
        return cur + 1
        # @lc code=end
