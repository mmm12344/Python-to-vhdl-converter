from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process
import time


class DFlipFlop():
    name = "DFlipFlop"
    inputs = [Input("clock", Std_logic()), Input("data", Std_logic())]
    outputs = [Output("q", Std_logic())]

class Arch():
    path = __file__
    signals = []
    name = "behavior"
    entity_name = "DFlipFlop"

@logic
def logic():
    @process
    def process(clock, data):
        if rising_edge(clock):
            q = data

save_to_file(Entity(DFlipFlop()), Architecture(Arch()))