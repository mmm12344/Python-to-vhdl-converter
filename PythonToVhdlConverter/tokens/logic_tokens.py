from tdparser import Token



class And_tok(Token):
    regexp = r"\band\b"
    lpd = 20
       
    def led(self, left, context):
        return left.text + " and " + self.text
    
class Not_tok(Token):
    regex = r"\bnot\b"
    lpd = 90
    
    def led(self, left, context):
        return left.text + " not " + self.text
    
class Or_tok(Token):
    regex = r"\bor\b"
    lpd = 20
    
    def led(self, left, context):
        return left.text + " or " + self.text
    
class Xor_tok(Token):
    regex = r"\b^\b"
    lpd = 20
    
    def led(self, left, context):
        return left.text + " xor " + self.text

class Nand_tok(Token):
    regex = r"\b|nand|\b"
    lpd = 20
    
    def led(self, left, context):
        return left.text + " nand " + self.text
    
class Nor_tok(Token):
    regex = r"\b|nor|\b"
    lpd = 20
    
    def led(self, left, context):
        return left.text + " nor " + self.text
    
class Xnor_tok(Token):
    regex = r"\b|xnor|\b"
    lpd = 20
    
    def led(self, left, context):
        return left.text, " xnor " + self.text

