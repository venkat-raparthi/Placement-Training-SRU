# class Stack:
#     def __init__(self):
#         self.items=[]

#     def is__empty(self):
#         return len(self.items)==0
    
#     def push(self,item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is__empty():
#             return self.items.pop()
#         else:
#             raise IndexError("Pop from an empty stack")

#     def peek(self):
#         if not self.is__empty():
#             return self.items[-1]
#         else:
#             raise IndexError("Peek from an empty stack")
        
#     def size(self):
#         return len(self.items)
    
# stack= Stack()
# print("Is the stack empty?", stack.is__empty())
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print("Stack:",stack.items)
# print("Top of the stack:",stack.peek())
# print("Pop:",stack.pop())
# print("Stack after pop:",stack.items)
# print("Is the stack empty?",stack.is__empty())
# print("Size of the stack:",stack.size())

def isValid(s):
    stack=[]
    pairs={
        '(':')',
        '{':'}',
        '[':']'
    }
    for bracket in s:
        if bracket in pairs:
            stack.append(bracket)
        elif stack and bracket==pairs[stack[-1]]:
            stack.pop()
        else:
            return False
        
    return not stack

