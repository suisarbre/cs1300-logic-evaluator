from logicalToken import *

class Tokenizer:
    # Tokenizes a logical expression
    def __init__(self, str):
        self.str = str
        self.tokens = []
        self.tokenize()
        self.postfix = self.to_postfix()
    def tokenize(self):
        i = 0
        while i < len(self.str):
            char = self.str[i]
            
            if char == ' ':
                i += 1
                continue
            
            elif char == '(':
                self.tokens.append(LogicalToken('LPAREN', char))
            
            elif char == ')':
                self.tokens.append(LogicalToken('RPAREN', char))
                
            elif char == '!' or char == '~':
                self.tokens.append(LogicalToken('NOT', char))
            
            elif char == '&':
                self.tokens.append(LogicalToken('AND', char))
                
            elif char == '|':
                self.tokens.append(LogicalToken('OR', char))
                
            elif char == '^':
                self.tokens.append(LogicalToken('XOR', char))
            
            elif char == '-':
                if i + 1 < len(self.str) and self.str[i + 1] == '>':
                    self.tokens.append(LogicalToken('IMPLIES', '->'))
                    i += 1  # Skip the next character because we consumed it
                else:
                    print("Error: invalid token")
                    break
            
            elif char == '<':
                if i + 2 < len(self.str) and self.str[i + 1] == '-' and self.str[i + 2] == '>':
                    self.tokens.append(LogicalToken('IFF', '<->'))
                    i += 2  # Skip the next two characters because we consumed them
                else:
                    print("Error: invalid token")
                    break
            
            else:
                self.tokens.append(LogicalToken('Prop', char))
            
            i += 1  # Move to the next character
                
    def to_postfix(self):
        precedence = {'NOT': 3, 'AND': 2, 'OR': 1, 'XOR': 1, 'IMPLIES': 0, 'IFF': 0}
        stack = []
        postfix = []
        
        for token in self.tokens:
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
    
    def __str__(self):
        return '\n'.join([str(token) for token in self.tokens])
    
if __name__ == "__main__":
    t = Tokenizer("!(p -> q) & (p | q) <-> (p ^ q)")
    t.tokenize()
    print(t)