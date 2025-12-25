import tokens as tok

class Lexer:
    def __init__(self, input) -> None:
        self.read_pos = 0
        self.input = input
        self.length = len(input)
        self.ch = self.read_char()

    def next_token(self) -> tok.Token:
        token = tok.Token(tok.ILLEGAL, self.ch)

        # Single char tokens
        match self.ch:
            case "(":
                token = tok.Token(tok.LPAREN, self.ch)
            case ")":
                token = tok.Token(tok.RPAREN, self.ch)
            case "{":
                token = tok.Token(tok.LBRACE, self.ch)
            case "}":
                token = tok.Token(tok.RBRACE, self.ch)
            case "[":
                token = tok.Token(tok.LBRACKET, self.ch)
            case "]":
                token = tok.Token(tok.RBRACKET, self.ch)
            case "\0":
                token = tok.Token(tok.EOF, self.ch)
            case "!":
                if self.peek_char() == "=":
                    neq = self.ch + self.read_char()
                    token = tok.Token(tok.NOT_EQ, neq)
                else:
                    token = tok.Token(tok.BANG, self.ch)
            case "=":
                if self.peek_char() == "=":
                    eq = self.ch + self.read_char()
                    token = tok.Token(tok.EQ, eq)
                else:
                    token = tok.Token(tok.ASSIGN, self.ch)

        # Multi char tokens
        if self.is_char(self.ch):
            word = self.read_word()
            tok_type = tok.keywords[word]
            token = tok.Token(tok_type, word)

        self.ch = self.read_char()

        return token

    def read_word(self) -> str:
        word = self.ch
        while self.is_char(self.ch):
            self.ch = self.read_char()
            word += self.ch

        return word

    def is_char(self, ch: str):
        """
        Determine if given input is a letter
        """

        is_lower = "a" <= ch <= "z"
        is_upper = "A" <= ch <= "Z"
        return is_lower and is_upper

    def read_char(self) -> str:
        """
        Get the next char to inspect
        """

        ch = self.__get_next_char()
        self.read_pos += 1
        return ch

    def peek_char(self) -> str:
        """
        Get the char one ahead of current position,
        Do not increment pointer
        """
        return self.__get_next_char()

    def __get_next_char(self):
        if self.length > self.read_pos:
            char = self.input[self.read_pos]
            return char

        return "\0"
