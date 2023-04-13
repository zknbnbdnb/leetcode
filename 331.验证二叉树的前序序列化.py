# @before-stub-for-debug-begin
from python3problem331 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == '':
            return False
        diff = 1
        preorder = preorder.split(',')
        for node in preorder:
            diff -= 1
            if diff < 0:
                return False
            if node != '#':
                diff += 2
        return diff == 0
# @lc code=end
