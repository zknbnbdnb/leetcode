/*
 * @lc app=leetcode.cn id=2488 lang=golang
 *
 * [2488] 统计中位数为 K 的子数组
 */

// @lc code=start
func countSubarrays(nums []int, k int) int {
	n := len(nums)
	d := make(map[int]int)
	d[0] = 1
	ans, pre := 0, 0
	p := 0
	for i, v := range nums {
		if v == k {
			p = i
			break
		}
	}
	for i := 0; i < p; i++ {
		if nums[i] < k {
			pre--
		} elif nums[i] > k {
			pre++
		}
		d[pre]++
	}
	for i := p; i < n; i++ {
		if nums[i] < k {
			pre--
		} elif nums[i] > k {
			pre++
		}
		ans += d[pre] + d[pre-1]
	}
	return ans

}

// @lc code=end

