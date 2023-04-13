/*
 * @lc app=leetcode.cn id=2540 lang=golang
 *
 * [2540] 最小公共值
 */

// @lc code=start
func getCommon(nums1 []int, nums2 []int) int {
	sort.Ints(nums1)
	sort.Ints(nums2)
	i, j := 0, 0
	for i < len(nums1) && j < len(nums2) {
		if nums1[i] == nums2[j] {
			return nums1[i]
		} else if nums1[i] < nums2[j] {
			i++
		} else {
			j++
		}
	}
	return -1
}

// @lc code=end

