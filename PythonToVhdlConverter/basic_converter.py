from .validation import validate_data_types


class Entity():
    def __init__(self, entity_class):
        self.entity_class = entity_class
        entity_structure = self.convert_entity()
    def convert_entity(self):
        return f"entity {self.entity_class.name} is\nport(\n{self.create_port()}\n)\nend {self.entity_class.name}"
    def create_port(self):
        port = ""
        for input in self.entity_class.inputs:
            port += input.__str__() + ";\n"
        for output in self.entity_class.outputs:
            port += "\n" + output.__str__() + ";"
        port = port[:-1]
        return port
        
        
        

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
