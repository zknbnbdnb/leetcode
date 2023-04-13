#
# @lc app=leetcode.cn id=2181 lang=python3
#
# [2181] 合并零之间的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        ans = []
        while head:
            res.append(head.val)
            head = head.next
        i = 0
        # 取ans中两个0中的间隔的数字之和
        while i < len(res):
            tmp = 0
            if res[i] == 0:
                j = i + 1
                while j < len(res) and res[j] != 0:
                    tmp += res[j]
                    j += 1
                if tmp != 0:
                    ans.append(tmp)
                i = j
            else:
                i += 1
        head = ListNode()
        cur = head
        for i in ans:
            cur.next = ListNode(i)
            cur = cur.next
        return head.next
# @lc code=end

