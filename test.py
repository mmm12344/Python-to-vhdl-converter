from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process, rising_edge, falling_edge
from PythonToVhdlConverter.components import mux4x1, JKFlipFlop, demux1x4
import time

@Entity
class mux4x1ux():
    name = "Mux"
    inputs = [Input("S", Std_logic())]
    outputs = [Output("F", Std_logic())]
 
@Architecture     
class Arch():
    path = __file__
    signals = [Signal("D", Std_logic_vector(3)), Signal("E", Std_logic())]
    name = "behavior"
    entity_name = "Mux"
               
@logic
def logic():
    
    a = b + a
    b = b << 1 >> 2
    
    a[0] == "10"
    
    a2 = 2
    
    if mario == 1:
        x = 0
    elif  mario == 2:
        x = 2
    else :
        x = 1
        
    A = not c
  
    A = 1
    
    rising_edge(mario)
    
    a_1 = 0

    mario = 30 ** 4 % 15 |sra| 40
        
    for i in range(1, 10):
        i = 1
        while i < 4:
            mario = 1
            while i < 4:
                mario = 1
            for i in range(1, 10):
                i = 1
        for i in range(1, 10):
            i = 1
            while i < 4:
                mario = 1
                for i in range(1, 10):
                    i = 1
        i = 5

    match i:
        case 3:
            mario = 3
        case 4:
            i = 5

    while i < 5:
        mario = 3
        while mario == 3:
            i = 5
            while i < 4:
                mario = 1
            for i in range(1, 10):
                i = 1
        
        while i < 4:
            mario = 1
        for i in range(1, 10):
            i = 1
        
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

save_to_file()
