/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	hash := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		if j, ok := hash[target-nums[i]]; ok {
			return []int{j, i}
		}
		hash[nums[i]] = i
	}
	return nil // 这里是为了编译通过，实际上不会执行到这里
}

// @lc code=end

