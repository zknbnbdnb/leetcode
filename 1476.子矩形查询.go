/*
 * @lc app=leetcode.cn id=1476 lang=golang
 *
 * [1476] 子矩形查询
 */

// @lc code=start
type SubrectangleQueries struct {
	rectangle [][]int
}

func Constructor(rectangle [][]int) SubrectangleQueries {
	return SubrectangleQueries{rectangle: rectangle}

}

func (this *SubrectangleQueries) UpdateSubrectangle(row1 int, col1 int, row2 int, col2 int, newValue int) {
	for i := row1; i < row2+1; i++ {
		for j := col1; j < col2+1; j++ {
			this.rectangle[i][j] = newValue
		}
	}

}

func (this *SubrectangleQueries) GetValue(row int, col int) int {
	return this.rectangle[row][col]

}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * obj := Constructor(rectangle);
 * obj.UpdateSubrectangle(row1,col1,row2,col2,newValue);
 * param_2 := obj.GetValue(row,col);
 */
// @lc code=end

