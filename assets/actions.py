# Created on 2026-01-03

import os, json

def directory_snap(file_name : str):
    saves_dir = os.path.join(os.path.dirname(__file__), "saves")
    file_path = os.path.join(saves_dir, file_name)
    return file_path

def load_game(player_name,user_data):
    try:
        file_path = directory_snap(player_name)
        file = open(file_path + ".json", "r")
    except FileNotFoundError:
        return 0
    for x in file:
        info_dict = json.loads(x)
    
    user_data.name = info_dict["name"]
    user_data.heat_rate = info_dict["heat_rate"]
    user_data.heat_max = info_dict["heat_max"]
    user_data.bits = info_dict["bits"]
    user_data.bits_multi = info_dict["bit_multi"]
    user_data.bit_cooldown = info_dict["bit_cooldown"]

    file.close()

def load_shop(player_name,user_data):
    try:
        file_path = directory_snap(player_name)
        file = open(file_path + "-shop.json", "r")
    except FileNotFoundError:
        return 0
    for x in file:
        info_dict = json.loads(x)

    user_data.shop_items[0] = info_dict["upgrade1"]
    user_data.shop_items[1] = info_dict["upgrade2"]

    file.close()
    

def save_game(user_data):
    file_path = directory_snap(user_data.name)
    try: 
        file = open(file_path + ".json", "x")
    except FileExistsError:
        file = open(file_path + ".json", "w")
    
    template = {
        "name" : user_data.name,
        "heat_rate" : user_data.heat_rate,
        "heat_max" : user_data.heat_max,
        "bits" : user_data.bits,
        "bit_multi" : user_data.bit_multi,
        "bit_cooldown" : 0.1 * user_data.heat_rate
         }
    file.write(json.dumps(template))

    file.close()

def save_shop(user_data):
    file_path = directory_snap(user_data.name)
    try: 
        file = open(file_path + "-shop.json", "x")
    except FileExistsError:
        file = open(file_path + "-shop.json", "w")
    
    template = {
        "upgrade1" : user_data.shop_items[0],
        "upgrade2" : user_data.shop_items[1],
         }
    file.write(json.dumps(template))

    file.close()