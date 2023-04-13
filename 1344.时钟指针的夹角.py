#
# @lc app=leetcode.cn id=1344 lang=python3
#
# [1344] 时钟指针的夹角
#

# @lc code=start
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = (hour % 12) * 30 + minutes / 2 # 时针每小时转30度，每分钟转0.5度
        minute_angle = minutes * 6
        angle = abs(hour_angle - minute_angle)
        return min(angle, 360 - angle)  
    

s = Solution()
print(s.angleClock(12, 30))
# @lc code=end

