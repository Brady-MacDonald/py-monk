from typing import NamedTuple


#TokenType Constants
LPAREN = "LPAREN"
RPAREN = "RPAREN"
EOF = "EOF"


class Token(NamedTuple):
    Type: str
    Literal: str
