from lexer import Lexer
import tokens as token
import unittest


class TestLexer(unittest.TestCase):
    def setUp(self) -> None:
        input = '''let five = 5;
                    let ten = 10;

                    let add = fn(x, y) {
                    x + y;
                    };

                    let result = add(five, ten);
                    !-/*5;
                    5 < 10 > 5;

                    if (5 < 10) {
                        return true;
                    } else {
                        return false;
                    }

                    10 == 10;
                    10 != 9;
                    "foobar" 
                    "foo bar"
                    [1, 2];
                    macro(x, y) { 
                        x + y; 
                    };
                    '''

        self.lex = Lexer(input)

    def test_next_token(self):
        tests = [
            token.Token(token.LET, "let"),
            token.Token(token.IDENT, "five"),
            token.Token(token.ASSIGN, "="),
            token.Token(token.INT, "5"),
            token.Token(token.SEMICOLON, ";"),
            token.Token(token.LET, "let"),
            token.Token(token.IDENT, "ten"),
            token.Token(token.ASSIGN, "="),
            token.Token(token.INT, "10"),
            token.Token(token.SEMICOLON, ";"),
            token.Token(token.LET, "let"),
            token.Token(token.IDENT, "add"),
            token.Token(token.ASSIGN, "="),
            token.Token(token.FUNCTION, "fn"),
            token.Token(token.LPAREN, "("),
            token.Token(token.IDENT, "x"),
            token.Token(token.COMMA, ","),
            token.Token(token.IDENT, "y"),
            token.Token(token.RPAREN, ")"),
            token.Token(token.LBRACE, "{"),
            token.Token(token.IDENT, "x"),
            token.Token(token.PLUS, "+"),
            token.Token(token.IDENT, "y"),
            token.Token(token.SEMICOLON, ";"),
            token.Token(token.RBRACE, "}"),
            token.Token(token.SEMICOLON, ";"),
            token.Token(token.LET, "let"),
            token.Token(token.IDENT, "result"),
            token.Token(token.ASSIGN, "="),
            token.Token(token.IDENT, "add"),
            token.Token(token.LPAREN, "("),
            token.Token(token.IDENT, "five"),
            token.Token(token.COMMA, ","),
            token.Token(token.IDENT, "ten"),
            token.Token(token.RPAREN, ")"),
            token.Token(token.SEMICOLON, ";"),
            token.Token(token.BANG, "!"),
            token.Token(token.MINUS, "-"),
            token.Token(token.SLASH, "/"),
            token.Token(token.ASTERISK, "*"),
            token.Token(token.INT, "5"),
            token.Token(token.SEMICOLON, ";"),
            token.Token(token.INT, "5"),
            token.Token(token.LT, "<"),
            token.Token(token.INT, "10"),
            token.Token(token.GT, ">"),
            token.Token(token.INT, "5"),
            token.Token(token.SEMICOLON, ";"),
            token.Token(token.IF, "if"),
            token.Token(token.LPAREN, "("),
            token.Token(token.INT, "5"),
            token.Token(token.LT, "<"),
            token.Token(token.INT, "10"),
            token.Token(token.RPAREN, ")"),
            token.Token(token.LBRACE, "{"),
            token.Token(token.RETURN, "return"),
            token.Token(token.TRUE, "true"),
            token.Token(token.SEMICOLON, ";"),
            token.Token(token.RBRACE, "}"),
            token.Token(token.ELSE, "else"),
            token.Token(token.LBRACE, "{"),
            token.Token(token.RETURN, "return"),
            token.Token(token.FALSE, "false"),
            token.Token(token.SEMICOLON, ";"),
            token.Token(token.RBRACE, "}"),
            token.Token(token.INT, "10"),
            token.Token(token.EQ, "=="),
            token.Token(token.INT, "10"),
            token.Token(token.SEMICOLON, ";"),
            token.Token(token.INT, "10"),
            token.Token(token.NOT_EQ, "!="),
            token.Token(token.INT, "9"),
            token.Token(token.SEMICOLON, ";"),
            token.Token(token.STRING, "foobar"),
            token.Token(token.STRING, "foo bar"),
            token.Token(token.LBRACKET, "["),
            token.Token(token.INT, "1"),
            token.Token(token.COMMA, ","),
            token.Token(token.INT, "2"),
            token.Token(token.RBRACKET, "]"),
            token.Token(token.SEMICOLON, ";"),
            token.Token(token.MACRO, "macro"), 
            token.Token(token.LPAREN, "("), 
            token.Token(token.IDENT, "x"), 
            token.Token(token.COMMA, ","), 
            token.Token(token.IDENT, "y"), 
            token.Token(token.RPAREN, ")"), 
            token.Token(token.LBRACE, "{"), 
            token.Token(token.IDENT, "x"), 
            token.Token(token.PLUS, "+"),
            token.Token(token.IDENT, "y"), 
            token.Token(token.SEMICOLON, ";"), 
            token.Token(token.RBRACE, "}"), 
            token.Token(token.SEMICOLON, ";"),
            token.Token(token.EOF, ""),
        ]

        for tok in tests:
            lexer_token = self.lex.next_token()
            self.assertEqual(tok.Literal, lexer_token.Literal)
            self.assertEqual(tok.Type, lexer_token.Type)

if __name__ == "__main__":
    unittest.main()
