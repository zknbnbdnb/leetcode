#
# @lc app=leetcode.cn id=2490 lang=python3
#
# [2490] 回环句
#

# @lc code=start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s_list = sentence.split()
        n = len(s_list)
        for i in range(n - 1):
            if s_list[i][-1] != s_list[i + 1][0]:
                return False
        if s_list[-1][-1] != s_list[0][0]:
            return False
        return True
# @lc code=end

