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

def convert_to_txt(file_path):
    with open(file_path, 'r') as f1:
        with open("input.txt", 'w') as f2:
            f2.write(f1.read())
            
def save_output(lines):
    with open("logic_out.txt", 'w') as file:
        file.writelines(lines)
        
def find_leading_white_space(line):
    return len(line) - len(line.lstrip())


def parse_file(file_path):
    convert_to_txt(file_path)
    lines = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        
    logic_index = lines.index("@logic\n")
    lines = lines[logic_index+2:]
    
    parsed_text = []
    for line in lines:
        print(line)
        if find_leading_white_space(line) < 2:
            break
        parsed_text.append(parse_text(line.strip()))
        
    print(parsed_text)
        
    return "\n".join(parsed_text)
        
        
            

            

        
    

    

    
