from PythonToVhdlConverter.basic_converter import Entity, Input, Output
from PythonToVhdlConverter.to_vhdl import convert_to_vhdl
import time



class Mux():
    def __init__(self):
        a = Input("A", "std_logic")
        b = Output("B", "std_logic")
        self.name = "Mux"
        self.inputs = [a]
        self.outputs = [b]
        
entity = Entity(Mux())

print(convert_to_vhdl(entity))
