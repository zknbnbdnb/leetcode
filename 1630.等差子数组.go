import "sort"

/*
 * @lc app=leetcode.cn id=1630 lang=golang
 *
 * [1630] 等差子数组
 */

// @lc code=start
func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {
	m = len(l)
	res = make([]bool, m)
	for i := 0; i < m; i++ {
		res[i] = false
	}
	for i := 0; i < m; i++ {
		res[i] = check(nums[l[i] : r[i]+1])
	}
	return res

}

func check(nums []int) bool {
	sort.Ints(nums)
	diff := nums[1] - nums[0]
	for i := 2; i < len(nums); i++ {
		if nums[i]-nums[i-1] != diff {
			return false
		}
	}
	return true
}

// @lc code=end

