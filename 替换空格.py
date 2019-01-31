'''
题目
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
#coding:utf-8

def method(string):
    l = list(string)
    for i, elm in enumerate(list):
        if elm == "":
            l[i] = "%20"

