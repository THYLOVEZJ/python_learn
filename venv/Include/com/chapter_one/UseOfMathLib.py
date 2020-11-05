# 题目描述
# 森森在学专业课的时候，发现一个神奇的函数，叫 Gamma 函数。
# 森森想知道 Gamma 函数的值。
#
# 输入
# 输入一行一个正整数 n ，表示森森想要知道的函数值。
#
# 输出
# 输出一行一个浮点数，表示 Gamma(n) 的值。
import math
n=int(input())
a=math.gamma(n)
print(a)