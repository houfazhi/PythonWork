import sys
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

def delstack(stack,order):
    s = ""
    c = stack.pop()
    while(c != '('):
        s = c + s
        c = stack.pop()
    s = s.rstrip(')')
    sp = s.split('|')
    if order == 0:
        print("{} {}-{}->{}".format('X', 'X', '~', order))
        print('Y')
        print("{} {}-{}->{}".format(order, order, '~', order+1) +
              " {}-{}->{}".format(order,sp[0], order) +
              " {}-{}->{}".format(order,sp[1], order))
        order += 1
        return stack,order

if __name__ == "__main__":
    order = 0;
    s = input()
    stack = Stack()
    i = 0
    while i < len(s):
        if s[i] == '(':
            while(s[i] != ')'):
                stack.push(s[i])
                i += 1
            stack.push(s[i])
            i += 1
        elif s[i] == '*':
            if s[i-1] == ')':
                stack,order = delstack(stack,order)
                i += 1
            elif i == 0:
                print("{} {}-{}->{}".format('X','X','~',order)+
                      " {}-{}->{}".format(order,s[i],order) +
                      " {}-{}->{}".format(order,'~',order+1))
                i += 1
                order += 1
            else:
                print("{} {}-{}->{}".format(order, order, '~', order+1) +
                      " {}-{}->{}".format(order+1, s[i], order+1) +
                      " {}-{}->{}".format(order+1, '~', order + 2))
                order += 2

        else:
            if order == 0:
                print("{} {}-{}->{}".format('X','X', s[i],0))
                print('Y')
                i += 1
                order += 1
            elif i == len(s)-1:
                print("{} {}-{}->{}".format(order, order, s[i], 'Y'))
                i += 1
            else:
                print("{} {}-{}->{}".format(order, order, s[i], order+1))
                i += 1
                order += 1
