/*
 * @lc app=leetcode.cn id=1598 lang=golang
 *
 * [1598] 文件夹操作日志搜集器
 */

// @lc code=start
func minOperations(logs []string) int {
	stack := []string{}
	for _, log := range logs {
		if log == "../" {
			if len(stack) > 0 {
				stack = stack[:len(stack)-1]
			}
		} else if log != "./" {
			stack = append(stack, log)
		}
	}
	return len(stack)

}

// @lc code=end

