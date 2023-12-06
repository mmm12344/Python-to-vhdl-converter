from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signals, Architecture
from PythonToVhdlConverter.to_vhdl import convert_to_vhdl
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic
import time



class Mux():
    def __init__(self):
        a = Input("A", "std_logic")
        b = Output("B", "std_logic")
        self.name = "Mux"
        self.inputs = [a]
        self.outputs = [b]
      
class Arch():
    def __init__(self):
        d = Signals("D", "std_logic")
        e = Signals("E", "std_logic")
        self.path = __file__
        self.signals = [d, e]
        self.name = "behavior"
        self.entity_name = "Mux"
        
        
@logic
def logic():
    a = b + a
    b = b << 1
    
    mario = 30 ** 4 % 15 |sra| 40
    
    
entity = Entity(Mux())
arch = Architecture(Arch())




print(convert_to_vhdl(entity, arch))
