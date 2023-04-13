/*
 * @lc app=leetcode.cn id=2181 lang=golang
 *
 * [2181] 合并零之间的节点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeNodes(head *ListNode) *ListNode {
	res, ans := []int{}, []int{}
	for head != nil {
		res = append(res, head.Val)
		head = head.Next
	}
	i := 0
	for i < len(res) {
		tmp := 0
		if res[i] == 0 {
			j := i + 1
			for j < len(res) && res[j] != 0 {
				tmp += res[j]
				j++
			}
			if tmp != 0 {
				ans = append(ans, tmp)
			}
			i = j
		} else {
			i++
		}
	}
	head = &ListNode{Val: 0}
	cur := head
	for _, v := range ans {
		cur.Next = &ListNode{Val: v}
		cur = cur.Next
	}
	return head.Next

}

// @lc code=end

