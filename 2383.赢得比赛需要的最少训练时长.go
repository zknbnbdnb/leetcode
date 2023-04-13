/*
 * @lc app=leetcode.cn id=2383 lang=golang
 *
 * [2383] 赢得比赛需要的最少训练时长
 */

// @lc code=start
func minNumberOfHours(initialEnergy int, initialExperience int, energy []int, experience []int) int {
	res := 0
	tt_e := 0
	for _, v := range energy {
		tt_e += v
	}
	if tt_e 	 initialEnergy {
		res += tt_e - initialEnergy + 1
	}
	for _, v := range experience {
		if v >= initialExperience {
			t := v - initialExperience + 1
			res += t
			initialExperience += t + v
		} else {
			initialExperience += v
		}
	}
	return res

}

// @lc code=end

