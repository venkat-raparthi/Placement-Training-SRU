# ^=3
# / * =2
# + -=1

# (A+B/C*(D+E)-F)

# SYMBOL  STACK    POSTFIX
# (        (          
# A        (+         A
# +        (+
# B        (+         AB
# /        (+/        AB
# C                   ABC
# *        (+/*       ABC/            / COMES OUT BECAUSE IT HAS SAME POWER AS * AND IT CAME FIRST
# (        (+*(
# D        (+*(      ABC/D
# +        (+*(+
# E        (+*(+     ABC/DE
# )        (+*(+)    ABC/DE+         + COMES OUT BECAUSE IT IS IN CLOSED BRACES
# -        (-         ABC/DE+*+      * COMES OUT FIRST BECAUSE IT HAS HIGHER POWER COMPARED TO - AND + COMES OUT SAME AS * 
# F                   ABC/DE+*+F
# )        (-)        ABC/DE+*+F-


# CODE FOR INFIX TO POSTFIX

from collections import deque

def infix_to_postfix(expression):
    def get_precedence(op):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        return precedence.get(op, 0)

    output = []
    stack = deque()

    for token in expression:
        if token.isnumeric():  # if the token is an operand (number ie ABC OR 123)
            output.append(token)
        elif token == '(':  # left parenthesis
            stack.append(token)
        elif token == ')':  # right parenthesis
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # remove '(' from stack
        else:  # operator
            while stack and stack[-1] != '(' and get_precedence(stack[-1]) >= get_precedence(token):
                output.append(stack.pop())
            stack.append(token)

    # pop all the operators left in the stack
    while stack:
        output.append(stack.pop())

    return ''.join(output)

# Example usage
expression = "3+5*2/(7-2)"
print(f"Infix: {expression}")
print(f"Postfix: {infix_to_postfix(expression)}")
