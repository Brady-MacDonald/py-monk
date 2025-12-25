from lexer import tokens


class Lexer:
    def __init__(self, input) -> None:
        self.read_pos = 0
        self.input = input
        self.length = len(input)
        self.ch = self.read_char()

    def next_token(self) -> tokens.Token:
        token = tokens.Token(tokens.ILLEGAL, self.ch)

        # Single char tokens
        match self.ch:
            case "(":
                token = tokens.Token(tokens.LPAREN, self.ch)
            case ")":
                token = tokens.Token(tokens.RPAREN, self.ch)
            case "{":
                token = tokens.Token(tokens.LBRACE, self.ch)
            case "}":
                token = tokens.Token(tokens.RBRACE, self.ch)
            case "[":
                token = tokens.Token(tokens.LBRACKET, self.ch)
            case "]":
                token = tokens.Token(tokens.RBRACKET, self.ch)
            case "<":
                token = tokens.Token(tokens.LT, self.ch)
            case ">":
                token = tokens.Token(tokens.GT, self.ch)
            case ";":
                token = tokens.Token(tokens.SEMICOLON, self.ch)
            case ":":
                token = tokens.Token(tokens.COLON, self.ch)
            case "*":
                token = tokens.Token(tokens.ASTERISK, self.ch)
            case "/":
                token = tokens.Token(tokens.SLASH, self.ch)
            case "-":
                token = tokens.Token(tokens.MINUS, self.ch)
            case "+":
                token = tokens.Token(tokens.PLUS, self.ch)
            case "\0":
                token = tokens.Token(tokens.EOF, self.ch)
            case "!":
                if self.peek_char() == "=":
                    neq = self.ch + self.read_char()
                    token = tokens.Token(tokens.NOT_EQ, neq)
                else:
                    token = tokens.Token(tokens.BANG, self.ch)
            case "=":
                if self.peek_char() == "=":
                    eq = self.ch + self.read_char()
                    token = tokens.Token(tokens.EQ, eq)
                else:
                    token = tokens.Token(tokens.ASSIGN, self.ch)

        # Multi char tokens
        if self.is_char(self.ch):
            word = self.read_word()
            tok_type = tokens.keywords[word]
            token = tokens.Token(tok_type, word)

        self.ch = self.read_char()

        return token

    def read_word(self) -> str:
        """
        Read continuous word
        """

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
        return is_lower or is_upper

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
