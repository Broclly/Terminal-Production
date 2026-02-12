# Created on 2026-01-03

import os, json

def directory_snap(file_name : str):
    try:
        saves_dir = os.path.join(os.path.dirname(__file__), "saves")
        file_path = os.path.join(saves_dir, file_name)
        return file_path
    except:
        print("Invalid input.")

def load_game(player_name,user_data):
    try:
        file_path = directory_snap(player_name)
        file = open(file_path + ".json", "r")
    except FileNotFoundError:
        return 0
    for x in file:
        info_dict = json.loads(x)
    
    try:
        user_data.name = info_dict["name"]
        user_data.heat_rate = info_dict["heat_rate"]
        user_data.heat_max = info_dict["heat_max"]
        user_data.bits = info_dict["bits"]
        user_data.bits_multi = info_dict["bit_multi"]
        user_data.bit_cooldown = info_dict["bit_cooldown"]
        user_data.super_bits = info_dict["super_bits"]
        user_data.super_bit_chnce = info_dict["super_bits_chance"]
        user_data.fuse_cnt = info_dict["fuse_cnt"]
    except:
        pass

    file.close()

def load_shop(player_name,user_data):
    try:
        file_path = directory_snap(player_name)
        file = open(file_path + "-shop.json", "r")
    except FileNotFoundError:
        return 0
    for x in file:
        info_dict = json.loads(x)

    try:
        user_data.shop_items[0][0] = info_dict["bit_upgrade1"]
        user_data.shop_items[0][1] = info_dict["bit_upgrade2"]
        user_data.shop_items[0][2] = info_dict["bit_upgrade3"]
    except:
        pass

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
        "bit_cooldown" : 0.1 * user_data.heat_rate,
        "super_bits" : user_data.super_bits,
        "super_bits_chance" : user_data.super_bit_chnce,
        "fuse_cnt" : user_data.fuse_cnt
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
        "bit_upgrade1" : user_data.shop_items[0][0],
        "bit_upgrade2" : user_data.shop_items[0][1],
        "bit_upgrade3" : user_data.shop_items[0][2],
        "s_bit_upgrade1" : user_data.shop_items[1][0],
         }
    file.write(json.dumps(template))

    file.close()

def clear_screen():
    temp = os.name
    if temp == "nt":
        os.system('cls')
    else:
        os.system('clear')
