from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process
import time


class Decoder3x8():
    name = "Decoder3x8"
    inputs = [Input("inp", Std_logic_vector(3))]
    outputs = [Output("opt", Std_logic_vector(8))]

class Arch():
    path = __file__
    signals = []
    name = "behavior"
    entity_name = "Decoder3x8"

@logic
def logic():
    @process
    def process(inp):
        match inp:
            case " 000 " :
             opt = "00000001"
            case  " 001 " :
             opt = "00000010"
            case  " 010 "  :
             opt = "00000100"
            case  " 011 "  :
             opt = "00001000"
            case " 100 " :
             opt = "00010000"
            case  " 101 " :
             opt = "00100000"
            case  " 110 "  :
             opt = "01000000"
            case  " 111 "  :
             opt = "10000000"
        