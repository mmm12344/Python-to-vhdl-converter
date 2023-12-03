import re

digits = "0123456789"
literals = "thequickbrownfoxjumpsoverthelazydog"
symbols = "_|<>-+*/%|^<>="
variable_regex_exp = "^([A-Z]|[a-z])+([0-9])*$"


arithmatic_operators = ['-', '+', '*', '/', '%', '**']
logical_operators = ['and', 'or', 'not', '|nand|', '|nor|', '^', '|xnor|']
bitwise_operators = ['<<', '>>', '|sla|', '|sra|']
assignment_operators = ['=']


class Lexer:
    def __init__(self, text):
        self.text = text.lstrip()
        self.pos = -1
        self.current_char = None
        self.advance()
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
        
    def make_tokens(self):
        tokens = []
        
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in digits:
                tokens.append(self.make_number())
            else:
                tokens.append(self.make_string())
                
        return tokens
                
    def make_number(self):
        num_str = ""
        dot_count = 0
        
        while self.current_char != None and self.current_char in digits + '.':
            if self.current_char == '.':
                if dot_count == 1:break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
            
        if dot_count == 0:
            return int(num_str)
        else:
            return float(num_str)
        
    def make_string(self):
        string = ''
        
        while self.current_char != None and (self.current_char in literals or self.current_char in symbols):
            string += self.current_char
            self.advance()
        
        if string in arithmatic_operators or string in logical_operators or string in bitwise_operators or string in assignment_operators:
            return string
        elif re.match(variable_regex_exp, string):
            return string
        else:
            raise Exception(f"Illegal string ({string})")


def generate_tokens(text):
    lexer = Lexer(text)
    tokens = lexer.make_tokens()
    
    return tokens


            
        
        
            