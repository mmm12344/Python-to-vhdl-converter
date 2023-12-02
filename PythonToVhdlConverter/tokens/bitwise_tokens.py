from tdparser import Token


class SRL_tok(Token):
    regexp = r"\b>>\b"
    lpd = 40
    
    def led(self, left, context):
        return left.text + " srl " + self.text
    
class SLL_tok(Token):
    regexp = r"\b<<\b"
    lpd = 40
    
    def led(self, left, context):
        return left.text + " sll " + self.text
    
class SRA_tok(Token):
    regex = r"\b|sra|\b"
    lpd = 40
    
    def led(self, left, context):
        return left.text + " sra " + self.text
    
class SLA_tok(Token):
    regex = r"\b|sla|\b"
    lpd = 40
    
    def led(self, left, context):
        return left.text + " sla " + self.text