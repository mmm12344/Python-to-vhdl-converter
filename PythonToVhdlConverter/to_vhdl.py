

def convert_to_vhdl(entity, arch):
    return entity.convert_entity() + "\n" + arch.convert_arch()