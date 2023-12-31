from . import files
import os

def convert_to_vhdl(entity, arch):
    return entity.convert_entity() + "\n" + arch.convert_arch()


def save_to_file():
    if not os.path.exists("results"):
        os.makedirs("results")
    for file in files:
        print(file["architicture"].file_name)
        with open("results/"+file["architicture"].file_name+".vhdl", "w") as f:
            f.writelines(convert_to_vhdl(file["entity"], file["architicture"]))