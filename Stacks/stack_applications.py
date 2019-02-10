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

def reverse(string):
    rev_str = ''

    stack = stacks.Stack()

    # push all the characters into the stack.
    for i in string:
        stack.push(i)

    # until the stack is empty, pop from stack and store it in rev_str.
    while not stack.isempty():
        rev_str += stack.pop()

    return rev_str

def balanced_brackets(string):
    stack = stacks.Stack() # initialise an empty stack.
    bracks = {'(':')', '{':'}', '[':']'} # initialise a opening and closing bracket dictionary.
    back_bracks = dict(zip(bracks.values(), bracks.keys())) # swap keys and values so that both way access is now easy.

    for i in string:
        if i in bracks: # if i is an opening bracket, push it to stack.
            stack.push(i)
        else:
            if i in back_bracks and stack.ismember(back_bracks[i]):
                # else, if it is closing bracket and its counterpart (open bracket) is in the stack, then pop that counter part.
                stack.pop()

    # in this way, simply opening brackets will be pushed and poped from the stack.    
    if stack.isempty():
        return True
    else:
        return False
