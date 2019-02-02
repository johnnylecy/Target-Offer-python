'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
'''
分析：
栈和队列差别在于pop（）的顺序。用S1 push, 将S1 pop到S2, S2和S1逆序，S1 push， S2 pop
'''
class Slt():
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    def change(self):
        while self.s1:
            self.push(self.s2, self.s1.pop())
    def push(self, s, elm):
            return s.append(elm)
    def pop(self):
        return self.s2.pop()

        