import sys
sys.path.append('Stacks')
sys.path.append('Stacks/LinkedLists')
from Stacks import stacks

def convert(infix):
    expr = '' # this is what we actually return.
    stack = stacks.Stack() # initialize a stack.

    for i in infix:
        if i.isalpha(): # if the character is an alphabet, add to expr.
            print('Adding {} to postfix expression'.format(i))
            expr += i
        else:
            if i is not ')': # if no closing bracket, continue to add to stack.
                print('Pushing {}'.format(i))
                stack.push(i)
            else:
                print('Popping')
                while stack.top() != '(': # continue poping till you get to (.
                    expr += stack.pop()
                stack.pop() # pop ( but don't add to expr.
        print('==========')
        print('Stack status...')
        stack.display()
        print('Status of postfix...')
        print(expr)
        print('==========')
    return expr
