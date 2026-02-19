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
        user_data.bonus_fuses = info_dict["bonus_fuses"]
        user_data.fuse_durability = info_dict["fuse_durability"]
        user_data.current_imbuement = info_dict["current_imbuement"]
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
        user_data.shop_items[1][0] = info_dict["s_bit_upgrade1"]
        user_data.shop_items[1][1] = info_dict["s_bit_upgrade2"]
        user_data.shop_items[1][2] = info_dict["s_bit_upgrade3"]
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
        "bonus_fuses" : user_data.bonus_fuses,
        "fuse_durability" : user_data.fuse_durability,
        "current_imbuement" : user_data.current_imbuement,
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
        "s_bit_upgrade2" : user_data.shop_items[1][1],
        "s_bit_upgrade3" : user_data.shop_items[1][2],
         }
    
    file.write(json.dumps(template))
    file.close()

def new_game(user):
    file_path = directory_snap(user)
    try: 
        file = open(file_path + "-shop.json", "x")
    except FileExistsError:
        file = open(file_path + "-shop.json", "w")
    
    template = {
        "bit_upgrade1" : {"tier" : 1, "cost" : 10, "id" : "Heat Rate"},
        "bit_upgrade2" : {"tier" : 1, "cost" : 25, "id" : "Bit Multi"},
        "bit_upgrade3" : {"tier" : 1, "cost" : 1000, "id" : "Super-Bit Chance"},
        "s_bit_upgrade1" : {"tier" : 1, "cost" : 1, "id" : "Xtra Fuse"},
        "s_bit_upgrade2" : {"tier" : 1, "cost" : 15, "id" : "Better Fuses"},
        "s_bit_upgrade3" : {"tier" : 1, "cost" : 10, "id" : "Super-Bit Chance II"}
         }
    file.write(json.dumps(template))
    file.close()

    try: 
        file = open(file_path + ".json", "x")
    except FileExistsError:
        file = open(file_path + ".json", "w")

    template = {
        "name" : user,
        "heat_rate" : 20,
        "heat_max" : 100,
        "bits" : 0,
        "bit_multi" : 1,
        "bit_cooldown" : 2,
        "super_bits" : 0,
        "super_bits_chance" : 0,
        "bonus_fuses" : 0,
        "fuse_durability" : 0,
        "current_imbuement" : "None",
         }
    
    file.write(json.dumps(template))
    file.close()

def clear_screen():
    temp = os.name
    if temp == "nt":
        os.system('cls')
    else:
        os.system('clear')