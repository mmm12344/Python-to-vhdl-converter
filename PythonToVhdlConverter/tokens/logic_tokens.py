from tdparser import Token


class And_tok(Token):
    regexp = r"and"
    lpd = 20
       
    def led(self, left, context):
        return left.text + " and " + context.text
    
class Not_tok(Token):
    regex = r"not"
    lpd = 90
    
    def led(self, left, context):
        return left.text + " not " + context.text
    
class Or_tok(Token):
    regex = r"or"
    lpd = 20
    
    def led(self, left, context):
        return left.text + " or " + context.text
    
class Xor_tok(Token):
    regex = r"\^"
    lpd = 20
    
    def led(self, left, context):
        return left.text + " xor " + context.text

class Nand_tok(Token):
    regex = r"|nand|"
    lpd = 20
    
    def led(self, left, context):
        return left.text + " nand " + context.text
    
class Nor_tok(Token):
    regex = r"|nor|"
    lpd = 20
    
    def led(self, left, context):
        return left.text + " nor " + context.text
    
class Xnor_tok(Token):
    regex = r"|xnor|"
    lpd = 20
    
    def led(self, left, context):
        return left.text, " xnor " + context.text

