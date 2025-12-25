from lexer import Lexer
from lexer import tokens


def main(input: str):
    """
    Entry point to program
    """

    lex = Lexer(input)
    tok = lex.next_token()
    while tok.Type != tokens.EOF:
        print(tok)
        tok = lex.next_token()


input = "let()==()"
main(input)
