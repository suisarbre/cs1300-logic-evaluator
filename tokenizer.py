from logicalToken import *

class Tokenizer:
    def __init__(self, str):
        self.str = str
        self.tokens = []
        
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
                
    def __str__(self):
        return '\n'.join([str(token) for token in self.tokens])
    
if __name__ == "__main__":
    t = Tokenizer("!(p -> q) & (p | q) <-> (p ^ q)")
    t.tokenize()
    print(t)