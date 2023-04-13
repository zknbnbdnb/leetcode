# @before-stub-for-debug-begin
from python3problem104 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        list = []
        temp = []
        i = 0

        def dfs(root, temp, list, i):
            if not root:
                return 0
            i += root.val
            temp.append(str(root.val))
            if not root.left:
                if not root.right:
                    list.append(i)
                    list.append('->'.join(temp))
            dfs(root.left, temp, list, i)
            dfs(root.right, temp, list, i)
            temp.pop()
            return list
        list = dfs(root, temp, list, i)
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
# @lc code=end
