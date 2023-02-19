# python3
# 221REB054 Marija Tulovska 13.gr
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    
    for i, inext in enumerate(text):
        if inext in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(inext, i+1))
            
            
        elif inext in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, inext):
                return i+1
            opening_brackets_stack.pop()

    if opening_brackets_stack:
        return opening_brackets_stack[-1].position
    return "Success"

def main():
    test = input()
    if ("I" in test):
        text = input()
        mismatch = find_mismatch(text)
        # Printing answer, write your code here
        print(mismatch)

if __name__ == "__main__":
    main()
