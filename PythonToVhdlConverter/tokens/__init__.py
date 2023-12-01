import tdparser
from logic_tokens import And_tok, Or_tok, Xor_tok


lexer = tdparser.Lexer(with_parens=True)
lexer.register_token(And_tok, Or_tok, Xor_tok)

def Parse(text):
    return lexer.parse(text)
