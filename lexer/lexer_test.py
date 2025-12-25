from lexer.lexer import Lexer
import tokens as t
import unittest


class TestLexer(unittest.TestCase):
    def setUp(self) -> None:
        input = "()!=[]"
        self.lex = Lexer(input)

    def test_next_token(self):
        token_list = [
            t.Token(t.LPAREN, "("),
            t.Token(t.RPAREN, ")"),
            t.Token(t.NOT_EQ, "!="),
            t.Token(t.LBRACKET, "["),
            t.Token(t.RBRACKET, "]"),
            t.Token(t.EOF, "\0"),
        ]

        # How to handle longer lexer tokens than list above

        for tok in token_list:
            lexer_token = self.lex.next_token()
            self.assertEqual(tok.Literal, lexer_token.Literal)
            self.assertEqual(tok.Type, lexer_token.Type)


if __name__ == "__main__":
    unittest.main()
