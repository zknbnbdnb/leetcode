#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        node = ListNode(0)
        node.next = head
        p1 = node
        lenght = 0
        while p1.next:
            lenght += 1
            p1 = p1.next
        if k % lenght == 0:
            return head
        p1.next = head
        p1 = node
        i = lenght - (k % lenght)
        while i:
            p1 = p1.next
            i -= 1
        result = ListNode(0)
        result.next = p1.next
        p1.next = None
        return result.next
# @lc code=end
