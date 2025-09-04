def isOperator(op):
    if op == "*" or op == "+" or op == "-" or op == "/" or op == "^":
        return True
    else:
        return False


def preToInfix(prefix):
    stack = []
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            new_s = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(new_s)
            i -= 1
    return stack.pop()


def postToInfix(postfix):
    stack = []
    i = 0
    while i < len(postfix):
        if not isOperator(postfix[i]):
            stack.append(postfix[i])
            i += 1
        else:
            new_s = "(" + stack.pop() + postfix[i] + stack.pop() + ")"
            stack.append(new_s)
            i += 1
    return stack.pop()


def inToPostfix(postfix):
    stack = []
    new_s = ""
    i = 0
    while i < len(postfix):
        if not isOperator(postfix[i]) and postfix[i] != '(' and postfix[i] != ')':
            new_s += postfix[i]
            i += 1
        elif postfix[i] == '(' or isOperator(postfix[i]):
            stack.append(postfix[i])
            i += 1
        elif postfix[i] == ')':
            while True:
                temp = stack.pop()
                if temp == '(':
                    break
                new_s += temp
            i += 1
    while stack:
        new_s += stack.pop()
    return new_s


def inToPrefix(prefix):
    prefix = prefix[::-1]
    stack = []
    new_s = ""
    i = 0
    while i < len(prefix):
        if not isOperator(prefix[i]) and prefix[i] != '(' and prefix[i] != ')':
            new_s += prefix[i]
            i += 1
        elif prefix[i] == ')' or isOperator(prefix[i]):
            stack.append(prefix[i])
            i += 1
        elif prefix[i] == '(':
            while True:
                temp = stack.pop()
                if temp == ')':
                    break
                new_s += temp
            i += 1
    while stack:
        new_s += stack.pop()
    new_s = new_s[::-1]
    return new_s


def postToPrefix(fix):
    return postToInfix(inToPrefix(fix))


def preToPostfix(fix):
    return preToInfix(inToPostfix(fix))


s = input("Enter equation: ")
start = input("What is the inital form? pre, post, or in?: ")
end = input("What is the final form? pre, post, or in?: ")

if start == end:
    print(s)
elif start == "pre" and end == "in":
    print(preToInfix(s))
elif start == "pre" and end == "post":
    print(preToPostfix(s))
elif start == "in" and end == "pre":
    print(inToPrefix(s))
elif start == "in" and end == "post":
    print(inToPostfix(s))
elif start == "post" and end == "pre":
    print(postToPrefix(s))
else:
    print(postToInfix(s))
