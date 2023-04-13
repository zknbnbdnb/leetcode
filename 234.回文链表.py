#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        i = 0
        j = len(val_list) - 1
        while i < j:
            if val_list[i] != val_list[j]:
                return False
            i += 1
            j -= 1
        return True
        # @lc code=end
