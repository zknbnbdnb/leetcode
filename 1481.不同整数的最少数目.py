#
# @lc app=leetcode.cn id=1481 lang=python3
#
# [1481] 不同整数的最少数目
#

# @lc code=start
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = Counter(arr)
        res = 0
        for i in sorted(d.values()):
            if k >= i:
                k -= i
            else:
                res += 1
        return res
# @lc code=end

