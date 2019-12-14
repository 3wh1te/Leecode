## Intro
### 1.
### 4.Median of Two Sorted Arrays（分而治之）

#### 解题思路：（关键问题在于边界的处理）

##### 自己的思路：

1. 取两个列表的中位数
2. 比较中位数大小
3. 大中位数舍去后面的部分，小的中位数舍去前面的部分，舍去的长度=短数组的中位数位置
4. 形成的新数组再进行如此操作
5. 终止条件：这个地方要考虑很多，比较复杂

##### 官方思路：

- 递归解法（简述一下思路）

  ​	首先要明确中位数的概念，也就是说该值左右两边的值的数量是一样的（当偶数的时候是中间两个值的平均值），所以前提条件就是要保证该值左右两边的值的数量相同，如何保证？
  $$
  假设 n>=m， i = 0 \sim m, j = \frac{m + n + 1}{2} - i ，有B[j−1]≤A[i] 且 \text{A}[i-1] \leq \text{B}[j]
  $$
  在次前提下，通过二分搜索搜索合适的i，直到找到满足条件的i，j为止，如果m+n为奇数：返回	max(A[*i*−1],B[*j*−1])，如果m+n为偶数：返回max(A[*i*−1],B[*j*−1])+min(A[*i*],B[*j*])/2。

  一共有三种情况：

  1. (j = 0 or i = m or B[j-1] <= A[i]) and (j = n or i = 0 or A[i-1] <= B[j]),条件满足，可以返回。（其中有一个边界值的情况下，就不用检查其中一个条件了）
  2. i > 0 且 j < n 的情况下，检查A[i-1] <= B[j]，证 i > 0 时 j < n，不满足 i 的范围往上加
  3. j > 0 且 i < m 的情况下，检查B[j-1] <= A[i]，证 j > 0 时 i < m，不满足 i 的范围往下减

  

  ### 5. Longest Palindromic Substring（DP）

  #### 解题思路

  ##### 自己的思路：（感觉自己思路简单一点）

  对于字符串中的一个字符：判断该字符是否为最长的回文开头，判断以该字符开头结尾的字符串是否为回文。如果是，更新最长回文，如果不是找下一个字符。

  ##### 官方思路：

  1. 暴力破解：不多叙述，复杂度*O*(*n*3)

  2. 动态规划：因为有 *P*(*i*,*j*)是回文，那么(*P*(*i*+1,*j*−1)是回文且*S*[i]*==*S*[j]*，所以对于字符串中的每一个字符，都可以以当前字符或与下一个字符一起为整个回文中心，扩展为更长的回文。

     也就是说对于单个字符P[i]来说肯定是回文，如果S[i] = S[i+1]，P[i,i+1]也是回文。对于每个字符都只有这两种情况成为回文中心，所以以这两种情况进行扩展，找到最长的回文。扩展方式就是如果P[i,j]是回文，下一次扩展就是P[i+1,j+1]。类似于扩散的感觉。

  ### 15. 3Sum（三数之和）

  ### 18. Divide Two Integers

  #### 解题思路

  ##### 自己的思路

  首先就要确定符号，同号正，异号负。

  其次判定一下特殊情况，溢出的情况-2<sup>32</sup>和-1的时候，返回2<sup>31</sup>- 1

  先每次翻倍去靠近被除数，也就是 division += division，2倍4倍8倍16倍32倍……当大于被除数的时候停止

  利用右移操作回到上一步的倍数 division = division >> 1，从division 一半开始，用距离distance表示每次移动的距离，distance = division >> 1，靠近被除数，division = division + distance ,之后每次distance减半。

  当大于被除数就减，小于被除数就加，不断靠近被除数，知道这distance等于1倍的除数，就停止，最终得到的值如果大于被除数，那么这个倍数-1就是结果，如果小于，那么这个值就是结果。

  ##### 举例：

  91 7

  同号为+，没有溢出

  开始翻倍 7 14 28 56 112，此时112大于91，停止，此时为16倍

  回到56，倍数为8，distance为28，开始靠近56小于91下一个是46+28=84，倍数为12倍，84小于91下一个是84+14 = 98，倍数为14倍，98大于91，下一个是98-7=91，倍数为13倍，7刚好是为一倍的除数，所以停止，此时91也刚好等于被除数，所以最终结果是13倍。

  ### 31.  Next Permutation

  ### 22. Generate Parentheses

  #### 解题思路

  ##### 自己思路

  先产生所有可能的括弧，再验证，删除不合格的括弧。

  验证括弧合格的思路：维护一个变量x，按顺序遍历括弧，遇到（就+1，遇到）就-1，如果值出现负数，该括弧不合格，遍历结束，如果最后x不等于0，也不合格，等于0就是合格的。

  ##### 官方思路

  递归产生括弧

  #### 代码


  ~~~
  class Solution:
    def generateParenthesis(self, n: int):
        p = '()'
        res = []
        index = []
  
        n = 2*n
        for i in range(n):
            if i < n/2:
                index.append(1)
            else:
                index.append(0)
  
        while index[-1] < 2:
            s = ''
            for i in range(n):
                s += p[index[i]]
            res.append(s)
            col = 0
            while col < n - 1 and index[col] == 1:
                index[col] = 0
                col += 1
            index[col] += 1
            while sum(index) != n/2:
                col = 0
                while col < n - 1 and index[col] == 1:
                    index[col] = 0
                    col += 1
                index[col] += 1
  
        res_last = []
        for s in res:
            if self.is_valid_parenthese(s):
                res_last.append(s)
        return res_last
  
    def is_valid_parenthese(self,s: str):
        if s[0] == ')':
            return False
        stack = ''
        for ss in s:
            if ss == '(':
                stack += ss
            elif stack != '':
                stack = stack[:-1]
            else:
                stack += ss
        if stack == '':
            return True
                
  ~~~

  ### 33.Search in Rotated Sorted Array

  #### 解题思路

  ##### 自己思路

  简答的说就是，先找到分界点的位置，然后看target在哪一边，设置好right和left，进行二分搜索。