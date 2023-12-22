from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process
import time

class Mux():
    name = "Mux"
    inputs = [Input("A", Std_logic())]
    outputs = [Output("B", Std_logic())]
      
class Arch():
    path = __file__
    signals = [Signal("D", Std_logic_vector(3)), Signal("E", Std_logic())]
    name = "behavior"
    entity_name = "Mux"
               
@logic
def logic():
    a = b + a
    b = b << 1 >> 2
    
    a[0] = "1"
    

    mario = 30 ** 4 % 15 |sra| 40
        
    for i in range(1, 10):
        i = 1

    match i:
        case 3:
            mario = 3
        case 4:
            i = 5

    while i < 5:
        mario = 3
        
    @process
    def process(x, y):
        if mario / 2 <= 2 :
            x = 0
        elif mario * 2 > 2 :
            x = 2
        else :
            y = 0

        match mario:
            case 3:
                i = 3
            case 4:
                mario = 5

        while mario < 5:
            i = 4
            
        mario = 5 * 20 |xnor| 1
            

        


save_to_file(Entity(Mux()), Architecture(Arch))
