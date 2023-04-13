/*
 * @lc app=leetcode.cn id=2130 lang=golang
 *
 * [2130] 链表最大孪生和
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func pairSum(head *ListNode) int {
	t := []int{}
	for head != nil {
		t = append(t, head.Val)
		head = head.Next
	}
	res := -1
	for i := 0; i < len(t)/2; i++ {
		res = max(res, t[i]+t[len(t)-i-1])
	}
	return res

}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end

