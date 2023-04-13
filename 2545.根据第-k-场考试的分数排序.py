#
# @lc app=leetcode.cn id=2545 lang=python3
#
# [2545] 根据第 K 场考试的分数排序
#

# @lc code=start
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x: -x[k])
# @lc code=end

