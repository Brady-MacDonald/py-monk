import lexer


def main(input: str):
    """
    Entry point to program
    """

    lex = lexer.Lexer(input)
    tok = lex.next_token()
    while tok.type != "EOF":
        print(tok)
        tok = lex.next_token()


input = "()()"
main(input)
