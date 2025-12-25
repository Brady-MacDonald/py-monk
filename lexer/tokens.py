from typing import NamedTuple

# Keywords
FUNCTION = "FUNCTION"
LET = "LET"
TRUE = "TRUE"
FALSE = "FALSE"
IF = "IF"
ELSE = "ELSE"
RETURN = "RETURN"
MACRO = "MACRO"

# Constants
ILLEGAL = "ILLEGAL"
EOF = "EOF"
IDENT = "IDENT"
INT = "INT"
STRING = "STRING"

# Operators
ASSIGN = "ASSIGN"
""" '=' """
PLUS = "PLUS"
MINUS = "MINUS"
BANG = "BANG"
""" ! """
ASTERISK = "ASTERISK"
SLASH = "SLASH"

LT = "LT"
GT = "GT"
EQ = "EQ"
""" '==' """
NOT_EQ = "NOT_EQ"
""" != """

COMMA = "COMMA"
""" , """
LPAREN = "LPAREN"
""" ( """
RPAREN = "RPAREN"
""" ) """
LBRACE = "LBRACE"
""" { """
RBRACE = "RBRACE"
""" } """
LBRACKET = "LBRACKET"
""" [ """
RBRACKET = "RBRACKET"
""" ] """
SEMICOLON = "SEMICOLON"
""" ; """
COLON = "COLON"
""" : """


class Token(NamedTuple):
    Type: str
    Literal: str


# Map keywords to there TokenType
keywords = {
    "let": LET,
    "true": TRUE,
    "false": FALSE,
    "let": LET,
    "if": IF,
    "else": ELSE,
    "return": RETURN,
}
