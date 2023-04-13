#
# @lc app=leetcode.cn id=2525 lang=python3
#
# [2525] 根据规则将箱子分类
#

# @lc code=start
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        Heavy = False
        Bulky = False
        if length >= 10000 or width >= 10000 or height >= 10000 or (length * width * height) >= 10**9:
            Bulky = True
        if mass >= 100:
            Heavy = True
        if Heavy and Bulky:
            return "Both"
        if Heavy:
            return "Heavy"
        if Bulky:
            return "Bulky"
        return "Neither"
# @lc code=end

