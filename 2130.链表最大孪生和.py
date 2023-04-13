#
# @lc app=leetcode.cn id=2130 lang=python3
#
# [2130] 链表最大孪生和
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        t = []
        while head:
            t.append(head.val)
            head = head.next
        res = -1
        for i in range(len(t) // 2):
            res = max(res, t[i] + t[~i])
        return res
            
# @lc code=end

