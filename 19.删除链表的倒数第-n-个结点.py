#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        p2 = head
        for i in range(n):
            p1 = p1.next
        if not p1:
            return head.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        if p2.next == p1:
            p2.next = None
            return head
        else:
            p2.next = p2.next.next
            return head

            # @lc code=end
