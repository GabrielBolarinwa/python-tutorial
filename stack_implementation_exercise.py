from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def is_match(ch1, ch2):
    match_dict = {")": "(", "]": "[", "}": "{"}
    return match_dict[ch1] == ch2


def reverse_string(string):
    stack = Stack()
    reversed_string = ""
    for letter in string:
        stack.push(letter)
    while stack.size() != 0:
        reversed_string += stack.pop()
    return reversed_string


def is_balanced(string):
    stack = Stack()
    opening_brackets = ["(", "{", "["]
    closing_brackets = [")", "}", "]"]
    for letter in string:
        if letter in opening_brackets:
            stack.push(letter)
        elif letter in closing_brackets:
            if not stack.size():
                return False
            if not is_match(letter, stack.pop()):
                return False
    return stack.size() == 0


print(reverse_string("We will conquer COVID-19"))
print(is_balanced("(a+b}"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
