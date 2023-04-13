/*
 * @lc app=leetcode.cn id=2562 lang=golang
 *
 * [2562] 找出数组的串联值
 */

// @lc code=start
func findTheArrayConcVal(nums []int) int64 {
	i, j := 0, len(nums)-1
	res := int64(0)
	for i < j {
		res += Concat(nums[i], nums[j])
		i++
		j--
	}
	if i == j {
		res += int64(nums[i])
	}
	return res

}
func Concat(a, b int) int64 {
	s := strconv.Itoa(a) + strconv.Itoa(b)
	t, _ := strconv.Atoi(s)
	return int64(t)
}

// @lc code=end

