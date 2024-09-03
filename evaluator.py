from logicalToken import *
from tokenizer import Tokenizer

class Evaluator:
    def __init__(self, str):
        self.str = str
        self.tokenizer = Tokenizer(str)
        self.tokenizer.tokenize()
        self.postfix = self.to_postfix()
        self.prop_values = {}
        
    def to_postfix(self):
        precedence = {'NOT': 3, 'AND': 2, 'OR': 1, 'XOR': 1, 'IMPLIES': 0, 'IFF': 0}
        stack = []
        postfix = []
        
        for token in self.tokenizer.tokens:
            if token.type == 'Prop':
                postfix.append(token)
            elif token.type == 'LPAREN':
                stack.append(token)
            elif token.type == 'RPAREN':
                while stack and stack[-1].type != 'LPAREN':
                    postfix.append(stack.pop())
                stack.pop()  # pop the 'LPAREN'
            else:  # it's an operator
                while stack and precedence.get(stack[-1].type, -1) >= precedence[token.type]:
                    postfix.append(stack.pop())
                stack.append(token)
        
        while stack:
            postfix.append(stack.pop())
        
        return postfix
    
    def rpn(self):
        stack = []
        for token in self.postfix:
            if token.type == 'Prop':    
                stack.append(token)
                token.bool = self.prop_values.get(token.value, False)
            else:
                if token.type == 'NOT':
                    operand = stack.pop()
                    token.bool = not operand.bool
                else:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    if token.type == 'AND':
                        token.bool = operand1.bool and operand2.bool
                    elif token.type == 'OR':
                        token.bool = operand1.bool or operand2.bool
                    elif token.type == 'XOR':
                        token.bool = operand1.bool != operand2.bool
                    elif token.type == 'IMPLIES':
                        token.bool = not operand1.bool or operand2.bool
                    elif token.type == 'IFF':
                        token.bool = operand1.bool == operand2.bool
                stack.append(token)
        return stack[0].bool
    
    def set_prop_values(self, values):
        self.prop_values = values
        
    
    
if __name__ == "__main__":
    e = Evaluator("!(p -> q) & (p | q) <-> (p ^ q)")
    # for tk in e.postfix:
    #     print(tk)
    e.set_prop_values({'p': True, 'q': False})
    print(e.rpn())
    