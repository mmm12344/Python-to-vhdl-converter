import tdparser
from .logic_tokens import And_tok, Or_tok, Xor_tok, Nand_tok, Nor_tok, Xnor_tok, Not_tok
from .bitwise_tokens import SLA_tok, SRA_tok, SLL_tok, SRL_tok


lexer = tdparser.Lexer(with_parens=True)
lexer.register_tokens(And_tok, Or_tok, Xor_tok, Nand_tok, Nor_tok, Xnor_tok, Not_tok, SLA_tok, SRA_tok, SLL_tok, SRL_tok)


def Parse(text):
    return lexer.parse(text)


