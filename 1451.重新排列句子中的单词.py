#
# @lc app=leetcode.cn id=1451 lang=python3
#
# [1451] 重新排列句子中的单词
#

# @lc code=start
class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        text = text.split(' ')
        text.sort(key=lambda x: len(x))
        text[0] = text[0].capitalize()
        return ' '.join(text)
# @lc code=end

