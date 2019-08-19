import sys
sys.path.insert(0, '../linked_lists/linkedlist')
import linkedlist

class Stack():
    def __init__(self):
        self.stack = linkedlist.LinkedList()

    def push(self, item):
        self.stack.append(item)

    def display(self):
        self.stack.display()

    def top(self):
        return self.stack.length() - 1

    def pop(self):
        item = self.stack.ret_val(self.top())
        self.stack.delete(self.top())
        return item

    def isEmpty(self):
        if self.top() == -1:
            return True
        else:
            return False

    def peek(self):
        return self.stack.ret_val(self.top())

class Utility():
    def __init__(self):
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
        self.stack = Stack()

    def isoperator(self, item):
        if not item.isalpha() and item not in ['(', ')']:
            return True
        else:
            return False

    def flag(self, i):
        try:
            if self.precedence[i] <= self.precedence[self.stack.peek()]:
                flag = True
            else:
                flag = False
        except KeyError:
            flag = False
        return flag

    def infix_to_postfix(self, infix):
        #stack = Stack()
        postfix = ''

        for i in infix:
            if i.isalpha():
                postfix += i
            elif i == '(':
                self.stack.push(i)
            elif i == ')':
                while not self.stack.isEmpty() and self.stack.peek() != '(': 
                    postfix += self.stack.pop()
                if not self.stack.isEmpty() and self.stack.peek() != '(': 
                    return -1
                else: 
                    self.stack.pop()
            else:        
                while(not self.stack.isEmpty() and self.flag(i)): 
                    postfix += self.stack.pop()
                self.stack.push(i)
            self.stack.display()
            
        while not self.stack.isEmpty():
            postfix += self.stack.pop()

        return postfix
