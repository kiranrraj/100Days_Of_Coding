# Title  : Evaluate Reverse Polish Notation
# Author : Kiran raj R.
# Date   : 19/07/2025


# Given an array of tokens representing an arithmetic expression in Reverse Polish Notation (postfix), 
# evaluate the expression and return the result. Valid operators are +, -, *, and /. 
# Each operand may be an integer or another expression.

# Main Logic
# 1. Push each number you see onto a stack.
# 2. When you see an operator, you pop the top two numbers, apply the operator, then push the result back.

def eval_rpn(tokens):

    stack = []

    for token in tokens:
        # if operator, pop two operands and apply
        if token in {"+", "-", "*", "/"}:
            # Pop the two most recent operands
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                res = a + b
            elif token == "-":
                res = a - b
            elif token == "*":
                res = a * b
            else:
                # convert to int to remove decimal values.
                res = int(a / b)

            stack.append(res)
        else:
            # if the token is a number, push its integer value
            stack.append(int(token))

    # final result is the only item left
    return stack[0]

if __name__ == "__main__":
    tests = [
        (["2","1","+","3","*"], 9),
        (["4","13","5","/","+"], 6),
        (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
    ]
    for toks, exp in tests:
        print(toks, "->", eval_rpn(toks), "(expected", exp, ")")

# Time: O(n), 
#   where n = number of tokens, since we do O(1) work per token.
# Space: O(n) As we push the numbers to a new list(stack)