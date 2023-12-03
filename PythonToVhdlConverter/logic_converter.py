
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
            

            

        
    

    

    
