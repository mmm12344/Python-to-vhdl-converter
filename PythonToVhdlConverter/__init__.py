from . import basic_converter, logic_converter, validation, to_vhdl
from .tokens import *
from .lexer import register_tokens
from .to_json import init_json

init_json()

register_tokens(
    and_tok,
    not_tok,
    or_tok,
    xor_tok,
    nand_tok,
    nor_tok,
    xnor_tok,
    
    srl_tok,
    sll_tok,
    sra_tok,
    sla_tok,
    
    plus_tok,
    minus_tok,
    mult_tok,
    div_tok,
    mod_tok,
    exp_tok,
    
    equalto_tok,
    notequalto_tok,
    lessthan_tok,
    greaterthan_tok,
    lessthanorequalto_tok,
    greaterthanorequal_tok,
    
    ass_tok,
    
    right_bracket_tok,
    left_bracket_tok,
    
    single_quotation_tok,
    double_quotation_tok,
)


