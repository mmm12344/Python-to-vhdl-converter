from .validation import validate_data_types
from .logic_converter import parse_file

def style(block):
    styled = [""]
    styled[1:] = block.splitlines(True)
    return "\t".join(styled)

class Entity():
    """
    A class representing an entity.
 
    Attributes:
        ?: ?
    """

    def __init__(self, entity_class):
        """
        Initializes an Entity object.
 
        Parameters:
            ?: ?
        """
        self.entity_class = entity_class
        entity_structure = self.convert_entity()
    def convert_entity(self):
        """
        Converts class (entity) to VHDL code.
 
        Args:
            self
 
        Returns:
            str: VHDL code for an entity.
        """
        return f"entity {self.entity_class.name} is\nport(\n{self.create_port()}\n)\nend {self.entity_class.name}"
    def create_port(self):
        """
        Creates VHDL port.
 
        Args:
            self
 
        Returns:
            str: The VHDL code for a port with inputs and outputs.
        """
        port = ""
        for input in self.entity_class.inputs:
            port += input.__str__() + ";\n"
        for output in self.entity_class.outputs:
            port += "\n" + output.__str__() + ";"
        port = port[:-1] # to avoid writing ';);'
        return style(port)
        
        
class Architecture():
    """
    A class representing an architecture.
 
    Attributes:
        ?: ?
    """
    def __init__(self, architecture_class):
        """
        Initializes an Architecture object.
 
        Parameters:
            ?:?
        """
        self.architecture_class = architecture_class
    def convert_arch(self):
        """
        Converts class (architecture) to VHDL code.
 
        Args:
            self
 
        Returns:
            str: The VHDL code for an architecture with signals.
        """
        return f"architecture {self.architecture_class.name} of {self.architecture_class.entity_name} is\n{self.create_signals()}\n\tbegin\n{parse_file(self.architecture_class.path)}\n\tend;"
    def create_signals(self):
        """
        Creates VHDL signals.
 
        Args:
            self
 
        Returns:
            str: The VHDL code for signals.
        """
        signals = ""
        for signal in self.architecture_class.signals:
            signals += signal.__str__() + ";\n"
        return style(signals)
            

class Input():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        validate_data_types(type)
    def __str__(self):
        return f"{self.name} : in {self.type}"
    
class Output():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        validate_data_types(type)
    def __str__(self):
        return f"{self.name} : out {self.type}"

class Signal():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        validate_data_types(type)
    def __str__(self):
        return f"signal {self.name} : {self.type}"