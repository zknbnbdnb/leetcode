/*
 * @lc app=leetcode.cn id=2225 lang=golang
 *
 * [2225] 找出输掉零场或一场比赛的玩家
 */

// @lc code=start
func findWinners(matches [][]int) [][]int {
	winner := make(map[int]int)
	loser := make(map[int]int)
	for _, match := range matches {
		winner[match[0]]++
		loser[match[1]]++
	}
	t_w, t_l := []int{}, []int{}
	for k, v := range loser {
		if v == 1 {
			t_l = append(t_l, k)
		}
	}
	for k, _ := range winner {
		if temp, ok := loser[k]; ok {
			continue
		} else {
			t_w = append(t_w, k)
		}
	}
	sort.Ints(t_w)
	sort.Ints(t_l)
	return [][]int{t_w, t_l}

}

// @lc code=end

