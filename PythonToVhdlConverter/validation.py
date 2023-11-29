
data_types = ["std_logic", "bit"]


def validate_data_types(type):
    if(type not in data_types):
        raise Exception("Not supported Data type")