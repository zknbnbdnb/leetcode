#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None or head == None:
            return head
        p1 = p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        mid = p1
        temp = p1.next
        while temp.next:
            cur = temp.next
            temp.next = cur.next
            cur.next = mid.next
            mid.next = cur
        p2 = p1.next
        p1.next = None
        p1 = head
        while p2:
            temp = p2.next
            p2.next = p1.next
            p1.next = p2
            p2 = temp
            p1 = p1.next.next
            # @lc code=end
