#
# @lc app=leetcode.cn id=1936 lang=python3
#
# [1936] 新增的最少台阶数
#

# @lc code=start
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        res = 0
        s = 0
        for i in range(len(rungs)):
            if rungs[i] - s > dist:
                res += (rungs[i] - s - 1) // dist
            s = rungs[i]
        return res
# @lc code=end

