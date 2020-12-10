'''
    栈（堆叠栈）
    特点：先进后出  LIOF 后进先出
    栈顶：增加和删除的操作都是在栈顶完成的
    栈底：
    抽象数据结构（ADT）：
    Stack():创建一个新的空栈，不需要参数，返回一个空栈
    push(item): 入栈 将新项添加到堆栈的顶部 添加元素,有参数，无返回值
    pop():删除栈顶的元素，无参数，返回被删除的元素，堆栈被修改
    peek():返回栈顶的元素，堆栈不被修改
    size():无参数，返回栈的长度，整数
    is_Empty():无参数，返回布尔值
'''

class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []

s = Stack()
s.push(1)
s.push(2)
print(s.size())
print(s.isEmpty())
print(s.pop())
print(s.size())
