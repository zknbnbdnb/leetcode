#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res, stack = 0, []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    res += 1
        return res + len(stack)
# @lc code=end
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        t = []
        for i in array:
            if i.isdigit():
                t.append(1)
            else:
                t.append(-1)
        d = {0: -1}
        ans, l, cur, n = 0, 0, 0, len(t)
        for i in range(n):
            cur += t[i]
            if cur in d:
                if i - d[cur] > ans:
                    ans = i - d[cur]
                    l = d[cur] + 1
            else:
                d[cur] = i
        return array[l: l + ans]
