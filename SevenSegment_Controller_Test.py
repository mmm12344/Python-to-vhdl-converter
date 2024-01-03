from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture , Constant
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector ,  Integer, Array
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
    signals = [Signal("count", Integer(0,9)),Signal("demux_output", Std_logic_vector(4)),] 
    """ 
      VHDL Representation
      signal count : integer range 0 to 9 := 0; it can signal count : std_logic_vector(3 downto 0) := "0000";
      signal demux_output : std_logic_vector(3 downto 0) := "0000";
    """
    constants = [Constant( "seven_segment_patterns" ,Array(0, 9, Std_logic_vector(7)))]
    name = "behavior"
    entity_name = "_7segController"
               
@logic
def logic():
    count = 0
    demux_output = "0000"
    
    seven_segment_patterns[0] = " 0000001 "
    seven_segment_patterns[1] = " 1001111 "
    seven_segment_patterns[2] = " 0010010 "
    seven_segment_patterns[3] = " 0000110 "
    seven_segment_patterns[4] = " 1001100 "
    seven_segment_patterns[5] = " 0100100 "
    seven_segment_patterns[6] = " 0100000 "
    seven_segment_patterns[7] = " 0001111 "
    seven_segment_patterns[8] = " 0000000 "
    seven_segment_patterns[9] = " 0000100 "

    def process( clk , rst ):
        if rst == '1':
                count = 0

        elif rising_edge(clk):
             if count == 9 :
                  count = 0
             else:
                  count = count + 1

        seg = seven_segment_patterns[count]
        anode = demux_output    


        
    
   
   
        

save_to_file()
