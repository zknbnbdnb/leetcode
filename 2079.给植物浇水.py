#
# @lc app=leetcode.cn id=2079 lang=python3
#
# [2079] 给植物浇水
#
from typing import List
# @lc code=start
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        i = 0
        c_capacity = capacity
        while i < len(plants):
            if plants[i] <= capacity:
                res += 1
                capacity -= plants[i]
                i += 1
            else:
                res += 2 * i
                capacity = c_capacity
        return res

s = Solution()
print(s.wateringPlants([2,2,3,3], 5))

# @lc code=end

