#
# @lc app=leetcode.cn id=2383 lang=python3
#
# [2383] 赢得比赛需要的最少训练时长
#

# @lc code=start
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        res = 0
        tt_e = sum(energy)
        res += sum(energy) + 1 - initialEnergy if tt_e >= initialEnergy else 0
        for i in experience:
            if i >= initialExperience:
                a = i - initialExperience + 1
                res += a
                initialExperience += i + a
            else:
                initialExperience += i
        return res
# @lc code=end

