#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        p1 = head
        # p2 = head.next
        while p1.next:
            if p1.val == p1.next.val:
                p1.next = p1.next.next
            else:
                p1 = p1.next
        return head
# @lc code=end
