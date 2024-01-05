from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process, rising_edge, falling_edge
from PythonToVhdlConverter.components import decoder3x8
import time

@Entity
class MemoryAddressDecoder():
    name = "MemoryAddressDecoder"
    inputs = [Input("address", Std_logic_vector(3))]
    outputs = [Output("S", Std_logic_vector(8))]
 
@Architecture     
class Arch():
    path = __file__
    signals = [Signal("D", Std_logic_vector(8))]
    name = "behavior"
    entity = MemoryAddressDecoder
               
@logic
def logic():
   decoderinst = decoder3x8(address,D)
   S = D



save_to_file()
        


