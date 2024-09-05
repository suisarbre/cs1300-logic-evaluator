from tokenizer import Tokenizer
from tokenType import TokenType
class CompoundProposition:
    # Represents a compound proposition.
    # Keep track of number of literals. It may store simplyfied version of the proposition.
    # It may also store the truth table of the proposition.
    def __init__(self, str):
        self.str = str
        self.tokenizer = Tokenizer(str)
        self.literal_count = {}
        self.simplified = []
        self.count_literals()
        
        
    def simplify(self):
        pass
    
    def count_literals(self):
        for token in self.tokenizer.tokens:
            if token.type == 'Prop':
                self.literal_count[token.value] = self.literal_count.get(token.value, 0) + 1
    