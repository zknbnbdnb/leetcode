/*
 * @lc app=leetcode.cn id=1344 lang=golang
 *
 * [1344] 时钟指针的夹角
 */

// @lc code=start
func angleClock(hour int, minutes int) float64 {
	hour_angle := float64(hour%12)*30 + float64(minutes)/2
	minute_angle := float64(minutes) * 6
	angle := math.Abs(hour_angle - minute_angle)
	return math.Min(angle, 360-angle)

}

// @lc code=end

