from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process
import time

class Mux():
    name = "Mux"
    inputs = [Input("A", "std_logic")]
    outputs = [Output("B", "std_logic")]
      
class Arch():
    path = __file__
    signals = [Signal("D", "std_logic"), Signal("E", "std_logic")]
    name = "behavior"
    entity_name = "Mux"
               
@logic
def logic():
    a = b + a
    b = b << 1
    
    mario = 30 ** 4 % 15 |sra| 40
    
    if mario == 1 :
        mario = 1 % 10
        x = 4
    elif mario == 2 :
        m = 1 << 2
    else :
        mario = 0
        x = 3
        
    for i in range(1, 10):
        i = 1

    match i:
        case 3:
            mario = 3
        case 4:
            i = 5
        
    @process
    def process(x, y):
        if mario / 2 <= 2 :
            x = 0
        else :
            y = 0

        match mario:
            case 3:
                i = 3
            case 4:
                mario = 5
            

        
        
entity = Entity(Mux())
arch = Architecture(Arch())

save_to_file(entity, arch)
