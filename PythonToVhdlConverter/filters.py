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
        
        
        

class Capture:
    def __init__(self, lines):
        self.lines = lines
        self.pos = -1
        self.current_line = None
        self.tokens = []
        self.advance()
        self.tokenize()
        
    def tokenize(self):
        while self.current_line != None:
            if If_condition_filter.is_if(self.current_line):
                self.tokens.append(If_condition_filter(self.capture_if()))
            elif For_loop_filter.is_for(self.current_line):
                self.tokens.append(For_loop_filter(self.capture_for()))
            elif Process_filter.is_process(self.current_line):
                self.advance()
                self.tokens.append(Process_filter(self.capture_process()))
            else:
                self.tokens.append(Statement_filter(self.current_line))
                self.advance()
        
    def advance(self):
        self.pos += 1
        self.current_line = self.lines[self.pos] if self.pos < len(self.lines) else None
    
    def get_leading_white_sapces(self, line):
        return len(line) - len(line.lstrip())
    
    def is_child(self, parent_line, child_line):
        if self.get_leading_white_sapces(parent_line) < self.get_leading_white_sapces(child_line):
            return True
        return False
    
    def capture_if(self):
        else_regex_exp = "\s*else :$"
        if_block_lines = []
        found_else = False
        else_line = ""
        
        while self.current_line != None:
            
            if found_else and (not self.is_child(else_line, self.current_line)):
                break
            if re.match(else_regex_exp, self.current_line):
                found_else = True
                else_line = self.current_line
    
            if_block_lines.append(self.current_line)

            self.advance()
        return if_block_lines
    
    def capture_for(self):
        
        for_block_lines = []     
        for_block_lines.append(self.current_line)
        for_line = self.current_line
        self.advance()
        
        while self.current_line != None:
            if not self.is_child(for_line, self.current_line):
                break
            for_block_lines.append(self.current_line)
            self.advance()
        
        return for_block_lines
    
    def capture_process(self):
        process_block_lines = []
        process_line = self.current_line
        self.advance()
        while self.current_line != None:
            if not self.is_child(process_line, self.current_line):
                break
            process_block_lines.append(self.current_line)
            self.advance()
        return process_block_lines
                
    
    def get_tokens(self):
        return self.tokens
    
    def parse(self):
        parsed_block = ""
        for token in self.tokens:
            parsed_block += token.parse()
        return parsed_block
                
            
    

class Statement_filter:
    def __init__(self, line):
        self.line = line
    def parse(self):
        return parse_text(self.line) +" ;\n"

class Process_filter:
    def __init__(self, lines):
        self.lines = lines 
        self.process_regex_exp = "\s*def .+/((.+)/):$"
        self.sensitivity_list = []
   
    def tokenize(self):
        self.sensitivity_list = re.match(self.process_regex_exp, self.lines[0]).group(1).split(',')
        self.tokens = Capture(self.lines[1:]).get_tokens()
    
    def parse(self):
        parsed_block = f"process ({','.join(self.sensitivity_list)})\n"
        for token in self.tokens:
            parsed_block += token.parse() + "\n"
        parsed_block += "end process;\n"
        return parsed_block
    
    def is_process(line):
        process_decorator_regex_exp = "\s*@process$"
        if re.match(process_decorator_regex_exp, line):
            return True
        return False
    
        

class If_condition_filter:
    def __init__(self, lines):
        self.lines = lines
        self.if_regex_exp = "\s*if (.+):$"
        self.elif_regex_exp = "\s*elif (.+):$"
        self.else_regex_exp = "\s*else :$"
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
                token = Condition_token(else_type)
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
        
        parsed_block += "end if;\n"
        return parsed_block
    
    def is_if(line):
        if_regex_exp = "\s*if (.+):$"
        if re.match(if_regex_exp, line):
            return True
        return False
    


class For_loop_filter:
    def __init__(self, lines):
        self.lines = lines
        self.for_regex_exp = "\s*for (.+) in range\((.+),(.+)\):"
        self.tokens = []
        self.tokenize()
    
    def tokenize(self):
        for line in self.lines:
            for_match = re.match(self.for_regex_exp, line)
            if for_match:
                token = For_loop_token(for_match.group(1), for_match.group(2), for_match.group(3))
                self.tokens.append(token)
            else:
                self.tokens[-1].add_statement(Statement_filter(line))

    def parse(self):
        parsed_block = ""
        for token in self.tokens:
            parsed_block += f"for {parse_text(token.parameter)} in {parse_text(token.from_var)} to {parse_text(token.to_var)} loop\n"
            for statement in token.statements:
                parsed_block += f"{statement.parse()}\n"
        
        parsed_block += "end loop;\n"
        return parsed_block
                
    def is_for(line):
        for_regex_exp = "\s*for (.+) in range\((.+),(.+)\):"
        if re.match(for_regex_exp, line):
            return True
        return False