import json

def init_json():
    json_data = {"inputs":{}, "outputs": {}, "signals": {}}
    save_json(json_data)
def get_json():
    json_data = {}
    with open("data.json", 'r') as f:
        json_data = json.load(f)
    return json_data
def save_json(json_data):
    with open("data.json", "w") as f:
        json.dump(json_data, f, indent=4)

    

def add_input(input):
    data = {input.name : {'type': input.type.__str__()}}
    json_data = get_json()
    json_data["inputs"].update(data)
    save_json(json_data)
    
def add_output(output):
    data = {output.name : {'type': output.type.__str__()}}
    json_data = get_json()
    json_data["outputs"].update(data)
    save_json(json_data)
    
def add_signal(signal):
    data = {signal.name : {'type': signal.type.__str__()}}
    json_data = get_json()
    json_data["signals"].update(data)
    save_json(json_data)
    
    
    