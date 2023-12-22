class Bit:
    def __init__(self):
        self.allowed_values = ['0', '1']
    def __repr__(self):
        return "bit"


class Std_logic:
    def __init__(self):
        self.allowed_values = ['U', 'X', '0', '1', 'Z', 'W', 'L', 'H', '-']
    def __repr__(self):
        return "std_logic"
    
class Std_logic_vector:
    def __init__(self, num_of_bits):
        self.allowed_values = ['U', 'X', '0', '1', 'Z', 'W', 'L', 'H', '-']
        self.num_of_bits = num_of_bits
    def __repr__(self):
        return f'std_logic_vector({self.num_of_bits} downto 0)'
    
    