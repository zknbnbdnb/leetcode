#
# @lc app=leetcode.cn id=1471 lang=python3
#
# [1471] 数组中的 k 个最强值
#

# @lc code=start
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        arr.sort(key=lambda x: (abs(x - m), x), reverse=True)
        return arr[:k]
# @lc code=end

