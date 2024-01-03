from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process, rising_edge, falling_edge
from PythonToVhdlConverter.components import demux1x4
import time

@Entity
class _7segController ():
    name = "_7segController"
    inputs = [Input("clk", Std_logic()),Input("rst", Std_logic()),Input("number", Std_logic_vector(4))]
    outputs = [Output("seg", Std_logic_vector(7)),Output("anode", Std_logic_vector(4))]
 
@Architecture     
class Arch():
    path = __file__
    signals = [Signal("count", Std_logic_vector(4)),Signal("D", Std_logic_vector(4)),] 
    """ 
      VHDL Representation
      signal count : integer range 0 to 9 := 0; it can signal count : std_logic_vector(3 downto 0) := "0000";
      signal demux_output : std_logic_vector(3 downto 0) := "0000";
    """
    name = "behavior"
    entity_name = "_7segController"
               
@logic
def logic():
   
   S = D
        

save_to_file()
