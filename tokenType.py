from enum import Enum, auto

class TokenType(Enum):
    """LPAREN, RPAREN, NOT, AND, OR, XOR, IMPLIES, IFF, Prop"""
    LPAREN = auto()
    RPAREN = auto()
    NOT = auto()
    AND = auto()
    OR = auto()
    XOR = auto()
    IMPLIES = auto()
    IFF = auto()
    Prop = auto()