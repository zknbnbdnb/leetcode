# @before-stub-for-debug-begin
from python3problem102 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        temp_result = [root]
        while temp_result:
            result.append([i.val for i in temp_result])
            next_level = []
            for i in temp_result:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            temp_result = next_level
        return result

        # @lc code=end
