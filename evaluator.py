from logicalToken import *
from tokenizer import Tokenizer
from compoundProposition import CompoundProposition

class Evaluator:
    def __init__(self, str):
        self.str = str
        # self.tokenizer = Tokenizer(str)
        # self.tokenizer.tokenize()
        # self.postfix = self.to_postfix()
        self.compound_prop = CompoundProposition(str)
        self.prop_values = {}
        
    
    
    def rpn(self):
        stack = []
        for token in self.compound_prop.tokenizer.postfix:
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
        
    def truth_table(self):
        for prop in self.compound_prop.literal_count:
            print(prop, end='\t')
        print(self.str)
        
        for i in range(2 ** len(self.compound_prop.literal_count)):
            
            # Convert integer to binary and remove '0b' prefix
            binary_str = bin(i)[2:]
            # Pad binary string with leading zeros to ensure it has length n
            binary_str = binary_str.zfill(len(self.compound_prop.literal_count))
            # print(binary_str, end='\t')
            for index, prop in enumerate(self.compound_prop.literal_count):
                self.prop_values[prop] = bool(int(binary_str[index]))
                print(self.prop_values[prop], end='\t')
            # print("Testing prop values: ", self.prop_values)
            print(bool(self.rpn()))
    
    
if __name__ == "__main__":
    e = Evaluator("(p ->q) & ((q -> r) -> (r -> p))")
    e.set_prop_values({'p': False, 'q': False, 'r': True})
    print(e.rpn())
    e.truth_table()