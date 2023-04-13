#
# @lc app=leetcode.cn id=2125 lang=python3
#
# [2125] 银行中的激光束数量
#

# @lc code=start
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        tmp = []
        for i in range(len(bank)):
            if j := bank[i].count('1'):
                tmp.append(j)
        if len(tmp) == 1:
            return 0
        for i in range(len(tmp) - 1):
            res += tmp[i] * (tmp[i] - 1)
        return res 


# @lc code=end

