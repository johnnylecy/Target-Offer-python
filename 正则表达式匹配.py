'''
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，
但是与"aa.a"和"ab*a"均不匹配
'''
'''
将x*视作一体， 将重复字符视为一体。比较样例和模板之间lenth， 分为样例大于等于小于模板三个情况；
首先匹配*。等于匹配就好；小于如果不匹配就匹配模板下一位；大于，匹配就好；
'''