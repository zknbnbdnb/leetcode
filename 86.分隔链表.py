#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        b_node = ListNode(0)
        s_node = ListNode(0)
        p1 = head
        p2 = b_node
        p3 = s_node
        while p1:
            if p1.val >= x:
                p2.next = ListNode(p1.val)
                p2 = p2.next
                p1 = p1.next
                continue
            if p1.val < x:
                p3.next = ListNode(p1.val)
                p3 = p3.next
                p1 = p1.next
                continue
        p3.next = b_node.next
        return s_node.next
# @lc code=end
