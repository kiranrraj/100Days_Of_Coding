# Title  : Reverse Polish Notation
# Author : Kiran raj R.
# Date   : 20/07/2025

# Evaluates the value of an arithmetic expression in Reverse Polish Notation (RPN).

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# Note that division between two integers should truncate toward zero.

# This solution uses a stack to hold numbers. We iterate through the list of tokens.
# If a token is a number, we convert it to an integer and push it onto the stack.
# If a token is an operator, we pop the top two numbers from the stack. 
# The first one popped is the right operand, and the second one is the left operand. 
# We perform the operation and push the result back onto the stack.
# After iterating through all tokens, the final result will be the only item left on the stack.


from typing import List
import operator

def eval_rpn(tokens: List[str]) -> int:
    stack = []
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda a, b: int(a / b)  # Division truncates toward zero
    }

    for token in tokens:
        if token in operators:
            # It's an operator, so pop operands and perform the operation.
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.append(result)
        else:
            # It's a number, so push it onto the stack.
            stack.append(int(token))
            
    # The final result is the last item remaining on the stack.
    return stack[0]

# --- Example Usage ---
rpn_expr1 = ["2", "1", "+", "3", "*"]
print(f"Expression: {rpn_expr1}")
print(f"Result: {eval_rpn(rpn_expr1)}") 