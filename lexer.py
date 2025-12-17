import tokens as tok


class Lexer:
    def __init__(self, input) -> None:
        self.input = input
        self.pos = 0

    def next_token(self) -> tok.Token:
        ch = self.read_char()

        # Single char tokens
        match ch:
            case "\0":
                return tok.Token(tok.RPAREN, ch)
            case "(":
                return tok.Token(tok.LPAREN, ch)
            case ")":
                return tok.Token(tok.RPAREN, ch)

        # Multi char tokens

        return tok.Token("Test", "(")

    def read_char(self) -> str:
        """
        Get the next char to inspect
        """

        inputLen = len(self.input)
        if inputLen > self.pos:
            char = self.input[self.pos]
            self.pos += 1
            return char

        return "\0"
