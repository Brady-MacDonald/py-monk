from lexer import Lexer
from tokens import EOF


def main(input: str):
    """
    Entry point to program
    """

    lex = Lexer(input)
    tok = lex.next_token()
    while tok.Type != EOF:
        print(tok)
        tok = lex.next_token()


input = "()==()"
main(input)
