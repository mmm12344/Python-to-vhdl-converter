from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signals, Architecture
from PythonToVhdlConverter.to_vhdl import convert_to_vhdl
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
        self.signals = [d, e]
        self.name = "behavior"
        self.entity_name = "Mux"
        
entity = Entity(Mux())
arch = Architecture(Arch())



print(convert_to_vhdl(entity, arch))