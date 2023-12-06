from .lexer import parse_text



class Infix():
    def __init__(self):
        self
        
nand = Infix()
nor = Infix()
xnor = Infix()  

sra = Infix()
sla = Infix()


def logic(func):
    return 0

def get_lines(file_path):
    """
    Reads file and returns lines.
 
    Args:
        file_path(str): path to the file to read from.
 
    Returns:
        list(str): lines
    """
    with open(file_path, 'r') as f1:
        lines = f1.readlines()
    return lines
            
def save_output(lines):
    with open("logic_out.txt", 'w') as file:
        file.writelines(lines)
        
def find_leading_white_space(line):
    """
    Calculates number of leading white space.
 
    Args:
        line(str): The line.
 
    Returns:
        int: The number of leading white space.
    """
    return len(line) - len(line.lstrip())


def parse_file(file_path):
    lines = get_lines(file_path)
        
    logic_index = lines.index("@+\n")
    lines = lines[logic_index+2:]
    
    parsed_text = []
    for line in lines:
        print(line)
        if find_leading_white_space(line) < 2:
            break
        parsed_text.append(parse_text(line.strip()))
        
    print(parsed_text)
        
    return "\n".join(parsed_text)
        
        
            

            

        
    

    

    
