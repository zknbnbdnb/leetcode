#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        head1 = ListNode(0)
        head2 = ListNode(0)
        temp1 = head1
        temp2 = head2
        p1 = head
        count = 1
        while p1:
            if count % 2 == 0:
                temp2.next = p1
                temp2 = temp2.next
            else:
                temp1.next = p1
                temp1 = temp1.next
            count += 1
            p1 = p1.next
        temp2.next = None
        temp1.next = head2.next
        return head1.next
        # @lc code=end
