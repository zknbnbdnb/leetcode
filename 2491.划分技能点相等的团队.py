#
# @lc app=leetcode.cn id=2491 lang=python3
#
# [2491] 划分技能点相等的团队
#

# @lc code=start
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s, n = sum(skill), len(skill)
        if n == 2:
            return skill[0] * skill[1]       
        skill.sort()
        if s % (n // 2) == 0:        
            l, r = 0, n - 1
            res = 0
            while l < r:
                if skill[l] + skill[r] != s // (n // 2):
                    return -1
                res += skill[l] * skill[r]
                l += 1
                r -= 1
            return res
        return -1
        
# @lc code=end

