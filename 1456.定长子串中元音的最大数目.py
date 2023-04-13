#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d = set("aiueo")
        tmp = res = sum([1 for i in s[:k] if i in d])
        for i in range(k, len(s)):
            if s[i] in d:
                tmp += 1
            if s[i - k] in d:
                tmp -= 1
            res = max(res, tmp)
        return res
# @lc code=end

