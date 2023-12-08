

def convert_to_vhdl(entity, arch):
    return entity.convert_entity() + "\n" + arch.convert_arch()


def save_to_file(entity, architecture):
    with open("result.vhdl", "w") as f:
        f.writelines(convert_to_vhdl(entity, architecture))