# @before-stub-for-debug-begin
from python3problem501 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        res = []
        temp = [root]
        while temp:
            for i in temp:
                res.append(i.val)
            next_l = []
            for i in temp:
                if i.left:
                    next_l.append(i.left)
                if i.right:
                    next_l.append(i.right)
            temp = next_l
        result = {}
        for key in res:
            result[key] = result.get(key, 0) + 1
        fin = []
        for key, val in result.items():
            if val == max(result.values()):
                fin.append(key)
        return fin

        # @lc code=end
