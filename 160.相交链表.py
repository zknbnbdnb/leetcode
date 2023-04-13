#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        count = 0
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            if p1 == None:
                count += 1
                p1 = headB
            if p2 == None:
                p2 = headA
                count += 1
            if count > 2:
                return None
        return p1
        # @lc code=end
