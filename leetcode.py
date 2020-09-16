# -*- coding: utf-8 -*-
"""
@Author: Sakuran
@File: leetcode.py
@Time: 2020/9/6 0:04
"""


class MinStack155:
    # 设计一个支持
    # push ，pop ，top
    # 操作，并能在常数时间内检索到最小元素的栈。
    #
    # push(x) —— 将元素
    # x
    # 推入栈中。
    # pop() —— 删除栈顶的元素。
    # top() —— 获取栈顶元素。
    # getMin() —— 检索栈中的最小元素。
    #  
    #
    # 示例:
    #
    # 输入：
    # ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    # [[], [-2], [0], [-3], [], [], [], []]
    #
    # 输出：
    # [null, null, null, null, -3, null, 0, -2]
    #
    # 解释：
    # MinStack
    # minStack = new
    # MinStack();
    # minStack.push(-2);
    # minStack.push(0);
    # minStack.push(-3);
    # minStack.getMin();
    # --> 返回 - 3.
    # minStack.pop();
    # minStack.top();
    # --> 返回
    # 0.
    # minStack.getMin();
    # --> 返回 - 2.

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack:
            self.minstack.append(x)
        if x < min(self.minstack):
            self.minstack.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


class Solution107:
#     给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
#     例如：
#     给定二叉树[3, 9, 20, null, null, 15, 7],
#
#     3
#    / \
#   9  20
#      / \
#     15  7
# 返回其自底向上的层次遍历为：
#
# [
#     [15, 7],
#     [9, 20],
#     [3]
# ]

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    def levelOrderBottom(self, root):
        if not root:
            return []
        queue = [root]
        result = [[]]
        while queue:
            tmp = []
            for _ in range(len(queue)):
                currentnode = queue.pop(0)
                tmp.append(currentnode.val)
                if currentnode.left:
                    queue.append(currentnode.left)
                if currentnode.right:
                    queue.append(currentnode.right)
            result = [tmp] + result
        return result[:-1]


class Solution739:
    # 请根据每日
    # 气温
    # 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用0
    # 来代替。
    #
    # 例如，给定一个列表temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是[1, 1, 4, 2, 1, 1, 0, 0]。
    #
    # 提示：气温列表长度的范围是[1, 30000]。每个气温的值的均为华氏度，都是在[30, 100]范围内的整数。

    def dailyTemperatures(self, T):
        result = [0] * len(T)
        stack = []  # 遍历每一天的温度，将天数存在栈中
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:  # 当有可比较的温度（栈不为空）且当前温度比栈顶（最低温度）高时，算出等待天数
                index = stack.pop()
                result[index] = i - index

            stack.append(i)  # 栈为空或比栈顶的温度还要低，就把这一天放到栈中，认为比这一天高的天数还没有出现
        return result


class Solution77:
    # 给定两个整数n和k，返回1...n中所有可能的k个数的组合。
    #
    # 示例:
    #
    # 输入:n = 4, k = 2
    # 输出:
    # [
    #     [2, 4],
    #     [3, 4],
    #     [2, 3],
    #     [1, 2],
    #     [1, 3],
    #     [1, 4],
    # ]

    def DFS(self, n, k, start, tempres, res):
        if len(tempres) == k:
            res.append(tempres[:])
            return
        for i in range(start, n + 1):
            if k - len(tempres) > n+1-i:
                break
            tempres.append(i)
            self.DFS(n, k, i+1, tempres, res)
            tempres.pop()
        return res

    def combine(self, n: int, k: int):
        res = []
        return self.DFS(n, k, 1, [], res)


class Solution150:
    # 根据逆波兰表示法，求表达式的值。
    #
    # 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
    # 输入: ["2", "1", "+", "3", "*"]
    # 输出: 9
    # 解释: 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
    def evalRPN(self, tokens) -> int:
        tmp = []
        for i in tokens:
            if i in '+-*/':
                num1 = int(tmp.pop())
                num2 = int(tmp.pop())
                if i == '+':
                    tmp.append(num1 + num2)
                if i == '-':
                    tmp.append(num1 - num2)
                if i == '*':
                    tmp.append(num1 * num2)
                if i == '/':
                    tmp.append(int(num2 / num1))
            else:
                tmp.append(int(i))
        return tmp[0]


class Solution200:
    # 给你一个由'1'（陆地）和'0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
    # 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
    # 此外，你可以假设该网格的四条边均被水包围。
    #
    # 输入:
    # [
    #     ['1', '1', '0', '0', '0'],
    #     ['1', '1', '0', '0', '0'],
    #     ['0', '0', '1', '0', '0'],
    #     ['0', '0', '0', '1', '1']
    # ]
    # 输出: 3
    # 解释: 每座岛屿只能由水平和 / 或竖直方向上相邻的陆地连接而成。
    def numIslands(self, grid) -> int:
        count = 0
        self.line = len(grid)
        self.row = len(grid[0])
        for x in range(self.line):
            for y in range(self.row):
                if grid[x][y] == '1':
                    # self.BFS(grid, x, y)
                    self.DFS(grid, x, y)
                    count += 1
        return count

    def BFS(self, grid, x, y):
        islands = []
        visted = set()
        islands.append((x, y))

        while islands:
            currentx, currenty = islands.pop(0)
            for l, r in [(currentx, currenty+1), (currentx, currenty-1), (currentx+1, currenty), (currentx-1, currenty)]:
                if (l,r) not in visted and 0<=l<self.line and 0<=r<self.row and grid[l][r] == '1':
                    grid[l][r] = '0'
                    islands.append((l, r))
                    visted.add((l, r))

    def DFS(self, grid, x, y):
        if x<0 or y<0 or x>=self.line or y>=self.row or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        self.DFS(grid, x + 1, y)
        self.DFS(grid, x - 1, y)
        self.DFS(grid, x, y + 1)
        self.DFS(grid, x, y - 1)


class Solution226:
#     翻转一棵二叉树。
#     输入：
#
#      4
#     / \
#    2   7
#   / \ / \
#  1  3 6  9
# 输出：
#
#     4
#    / \
#   7   2
# /  \ / \
# 9  6 3  1

    def invertTree(self, root):
        queue = []
        result = []
        queue.append(root)
        result.append(root.val)

        while queue:
            current = queue.pop(0)
            if current.right:
                queue.append(current.right)
                result.append(current.right.val)
                print(result)
            if current.left:
                queue.append(current.left)
                result.append(current.left.val)
                print(result)

        print(result)
        return result

if __name__ == '__main__':
    demo = Solution200()
    res = demo.numIslands([['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']])
    print(res)