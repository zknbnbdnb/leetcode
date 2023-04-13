#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        d = set('aeiouAEIOU')
        res = []
        for i, word in enumerate(sentence.split()):
            if word[0] in d:
                res.append(word + 'ma' + 'a' * (i + 1))
            else:
                res.append(word[1:] + word[0] + 'ma' + 'a' * (i + 1))
        return ' '.join(res)
# @lc code=end

