# @before-stub-for-debug-begin
from python3problem662 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        temp = [root]
        while temp:
            res.append([i.val if i else None for i in temp])
            next_l = []
            for i in temp:
                if not i:
                    continue
                next_l.append(i.left if i.left else None)
                next_l.append(i.right if i.right else None)
            count = 0
            for i in next_l:
                if not i:
                    count += 1
            if count == len(next_l):
                break
            temp = next_l
        fin = []
        for i in res:
            fin.append(len(i))
        return max(fin)
# @lc code=end
