/*
 * @lc app=leetcode.cn id=2475 lang=golang
 *
 * [2475] 数组中不等三元组的数目
 */

// @lc code=start
func unequalTriplets(nums []int) int {
	res := 0
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			for k := j + 1; k < len(nums); k++ {
				if nums[i] != nums[j] && nums[j] != nums[k] && nums[i] != nums[k] {
					res++
				}
			}
		}
	}
	return res

}

// @lc code=end

