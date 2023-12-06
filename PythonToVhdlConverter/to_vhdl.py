

def convert_to_vhdl(entity, arch):
    return entity.convert_entity() + "\n" + arch.convert_arch()


def save_to_file(entity, architecture):
    with open("result.txt", "w") as f:
        f.writelines(convert_to_vhdl(entity, architecture))