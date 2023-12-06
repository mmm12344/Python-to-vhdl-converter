import re
from .lexer import parse_text

## if condition types

if_type = "if"
elif_type = "elif"
else_type = "else"

class Condition_token:
    def __init__(self, type, condition=None):
        self.condition = condition
        self.type = type
        self.statements = []
        
        
    def add_statement(self, statement):
        self.statements.append(statement)
        

class For_loop_token:
    def __init__(self, parameter, from_var, to_var):
        self.parameter = parameter
        self.from_var = from_var
        self.to_var = to_var
        self.statements = []
    
    def add_statement(self, statement):
        self.statements.append(statement)



class Statement_filter:
    def __init__(self, line):
        self.line = line
    def parse(self):
        return parse_text(self.line) +" ;"

class Process_filter:
    def __init__(self, sensitivity_list, lines):
        self.sensitivity_list = sensitivity_list
        self.lines = lines
        self.pos = -1
        self.current_line = None
        self.tokens = []
        self.advance()
        self.tokenize()
        
    def advance(self):
        self.pos += 1
        self.current_line = self.lines[self.pos] if self.pos < len(self.lines) else None
        
    def tokenize(self):
        while self.current_line != None:
            if not If_condition_filter.is_if(self.current_line):
                self.tokens.append(Statement_filter(self.current_line))
                self.advance()
            else:
                self.capture_if()
        

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
                token = Condition_token(if_type, if_match.group(1))
            elif elif_match:
                token = Condition_token(elif_type, elif_match.group(1))
            elif else_match:
                token = Condition_token(else_type, else_match.group(1))
            else:
                self.tokens[-1].add_statement(Statement_filter(line))
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
                parsed_block += f"{statement.parse()}\n"
        
        parsed_block += "end if\n"
        return parsed_block
    
    def is_if(self, line):
        if re.match(self.if_regex_exp, line) or re.match(self.elif_regex_exp, line) or re.match(self.else_regex_exp, line):
            return True
        return False
    


class For_loop_filter:
    def _init_(self, lines):
        self.lines = lines
        self.for_regex_exp = "^for (.+) in range/((.+),(.+)/):$"
        self.tokens = []
        self.tokenize()
    
    def tokenize(self):
        for line in self.lines:
            for_match = re.match(self.for_regex_exp, line)
            if for_match:
                token = For_loop_token(for_match.group(1), for_match.group(2), for_match.group(3))
                self.tokens.append(token)
            else:
                token[-1].add_statement(Statement_filter(line))

    def parse(self):
        parsed_block = ""
        for token in self.tokens:
            parsed_block += f"for {parse_text(token.parameter)} in {parse_text(token.from_var)} to {parse_text(token.to_var)} loop\n"
            for statement in token.statements:
                parsed_block += f"{statement.parse()}\n"
        
        parsed_block += "end loop;\n"
        return parsed_block
                
                