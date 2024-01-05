from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture, Constant
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector, Integer, Array
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process, rising_edge, falling_edge
from PythonToVhdlConverter.components import mux4x1, demux1x4, JKFlipFlop
import time

@Entity
class Mux():
    name = "Mux"
    inputs = [Input("A", Std_logic()), Input("C", Integer(0, 9)), Input("F", Integer())]
    outputs = [Output("B", Std_logic())]
 
@Architecture     
class Arch():
    path = __file__
    signals = [Signal("D", Std_logic_vector(3)), Signal("E", Std_logic())]
    constants = [Constant( "seven_segement_pattern" ,Array(0, 9, Std_logic_vector(7)))]
    name = "behavior"
    entity = Mux

@logic
def logic():
    
    time.sleep(2)
    
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

    match (b):
        case "00":
            y = "1000"
        case "01":
            y = "0100"
        case "10":
            y = "0110"
        case "11":
            y = "1001"

    
                
    @process
    def process(clock):
        
        qmario = TMP
        qkdjfksjf = not TMP 
        
        if j == '0' and k == '0' :
            TMP = TMP
        elif j == '1' and k == '1' :
            TMP = not TMP
        elif j == '0' and k == '1' : 
            TMP = '0'
        else:
            TMP = '1'
        qmario = TMP
        qkdjfksjf = not TMP 

        mario = 9
        a = 3
        match (a):
            case "00":
                m = "1000"
            case "01":
                m = "0100"
                match (a):
                    case "00":
                        m = "1000"
                        match (a):
                            case "00":
                                m = "1000"
                            case "01":
                                m = "0100"
                    case "01":
                        m = "0100"
            case "10":
                m = "0010"
            case "11":
                m = "0001"

    match (a):
                case "00":
                    m = "1000"
                case "01":
                    m = "0100"
                case "10":
                    m = "0110"
                case "11":
                    m = "1001"
        
    @process
    def process(clock):
        if rising_edge(clock):
            if j == '0' and k == '0' :
                TMP = TMP
            elif j == '1' and k == '1' :
                TMP = not TMP
            elif j == '0' and k == '1' : 
                TMP = '0'
            else:
                TMP = '1'

            match (a):
                case "00":
                    m = "1000"
                case "01":
                    m = "0100"
                case "10":
                    m = "0110"
                case "11":
                    m = "1001"
        q = TMP
        q = not TMP    
        
        match (a):
            case "01":
                if mario == 2:
                    x = 0
    c1 = mux4x1(mario[0], m , ar)
    
    match (b):
        case "00":
            y = "1000"
        case "01":
            y = "0100"
        case "10":
            y = "0110"
        case "11":
            y = "1001"
            
    f = (a + b)
        
          

save_to_file()
