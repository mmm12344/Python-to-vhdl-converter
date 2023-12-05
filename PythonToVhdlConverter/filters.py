import re
from .lexer import parse_text

## if condition types

if_type = "if"
elif_type = "elif"
else_type = "else"


class Condition:
    def __init__(self, type, condition=None):
        self.condition = condition
        self.type = type
        self.statements = []
        
    def add_statement(self, statement):
        self.statements.append(statement)
        

class If_condition_filter:
    def __init__(self, lines):
        self.lines = lines
        self.if_regex_exp = "^if (.+):$"
        self.elif_regex_exp = "^elif (.+):$"
        self.else_regex_exp = "^else (.+):$"
        self.tokens = []
        self.tokenize()
    
    def tokenize(self):
        for line in self.lines:
            if_match = re.match(self.if_regex_exp, line)
            elif_match = re.match(self.elif_regex_exp, line)
            else_match = re.match(self.else_regex_exp, line)
            if if_match:
                token = Condition(if_type, if_match.group(1))
            elif elif_match:
                token = Condition(elif_type, elif_match.group(1))
            elif else_match:
                token = Condition(else_type, else_match.group(1))
            else:
                self.tokens[-1].add_statement(line)
                continue
            self.tokens.append(token)

    def parse(self):
        parsed_block = ""
        for token in self.tokens:
            if token.type == if_type or token.type == elif_type:
                parsed_block += f"if {parse_text(token.condition)} then\n"
            elif token.type == else_type:
                parsed_block += f"else\n"
                
            for statement in token.statements:
                parsed_block += f"{parse_text(statement)}\n"
        
        parsed_block += "end if\n"
        return parsed_block
                
                