#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i
        for i, num in enumerate(nums):
            diff = target-num
            j = hashmap.get(diff)
            if(j and j != i):
                return[i, j]


# @lc code=end
'''
心得：学会建立哈希表
使用enumerate的for循环
'''
