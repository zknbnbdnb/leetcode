#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return self.bulidTree(res)

    def bulidTree(self, res):
        if len(res) == 0:
            return None
        elif len(res) == 1:
            return TreeNode(res[0])
        elif len(res) == 2:
            root = TreeNode(res[0])
            if res[0] < res[1]:
                root.right = TreeNode(res[1])
            if res[0] > res[1]:
                root.left = TreeNode(res[1])
            return root
        else:
            root = TreeNode(res[len(res) // 2])
            root.left = self.bulidTree(res[0: len(res) // 2])
            root.right = self.bulidTree(res[len(res) // 2 + 1:])
        return root
# @lc code=end
