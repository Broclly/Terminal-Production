# Created on 2026-02-05

import math, time, os, random
from assets import actions

scaling_mod = 0.31
imbument_list = [[{"name" : "Deep Freeze", "Desc" : "Divides heat by 4", "rarity" : "Common"}, {"name" : "Upgraded Multi", "Desc" : "Increases multi by +2x", "rarity" : "Common"}], [{"name" : "Work Smarter", "Desc" : "Increases fuse count by +3", "rarity" : "Uncommon"}, {"name" : "Flameborne", "Desc" : "+1% Increase for Super Bits every 10 Heat, instead of +0.1%", "rarity" : "Uncommon"}], [{"name" : "Superior Multi", "Desc" : "+2x Super Bit Multi, 1.5x Current Bit Multi (Upgrades people, Upgrades!)", "rarity" : 3}, {"name" : "Nudging the Scales", "Desc" : "+10% Super Bit Chance (Nothing wrong with a bit of cheating)" , "rarity" : "Rare"}], [{"name" : "Omnibus pro Unus et Unus pro Nemine", "Desc" : "Sacrifices half of your bit multi, -2 Fuses, and Grants 4x Super Bit Multi, +20% Super Bit Chance (it's like some type of... Bait & Switch)", "rarity" : "Legendary"}, {"name" : "Natus ex igne et flamma", "Desc": "Heat is generated 2 times faster, but heat now gives +2.5% Super Bit chance every 10 heat, and MAX heat is increased by 100", "rarity" : "Legendary"}]]
equipment_list = [[{"name" : "Super Amulet", "Desc" : "Grants +3 Super Bit Multi", "rarity" : "Common"}], [{"name" : "Fused-Iron Ring", "Desc" : "Grants +8 Fuse Durability", "rarity" : "Uncommon"}], [{"name" : "Molten Charm", "Desc" : "Grants +25 MAX heat, Allows the collection of 'Molten Bits' from production", "rarity" : "Rare"}]]

def shop_menu(data):
    while True:
        actions.clear_screen()
        print("Which shop will you go to?")
        print("1. Bitsclusives")
        print("2. Super-Shinies")
        print("3. Imbumental Forge")
        print("4. Back to menu")
        try:
            shop_selection = int(input("Select the number on which shop you'd like to visit: "))
        except ValueError:
            print("Invalid input.")
            time.sleep(3/2)
            actions.clear_screen()
        if shop_selection == 1:
            bitsclusives(data)
            return
        elif shop_selection == 2:
            supershinies(data)
            return
        elif shop_selection == 3:
            imbumentalforge(data)
            return
        elif shop_selection == 4:
            return

def bitsclusives(data):
    while True:
        actions.clear_screen()
        print("Brushia: Welcome to the Bitsclusives!")
        print(f"Bits: {int(data.bits)}")
        print("")
        iterator = 0
        for x in data.shop_items[0]:
            cost = math.floor(x["cost"] + (5 ** (scaling_mod * x["tier"])))
            print(f"Item #{iterator + 1}. {x["id"]} (Tier: {x["tier"]}) (Cost: {cost})")
            iterator += 1
        print("\n1. Buy item")
        print("2. Back to the menu")
        try:
            action = int(input("Select the number on which task you selected: "))
            if action == 1:
                try: 
                    action = int(input("Brushia: Which item would you like? (#): "))
                    amnt = input("Brushia: How many of those? (# or max): ")
                    shop_purchase(action, data, amnt, 1)
                except ValueError:
                    print("Invalid input.")
                    time.sleep(1)
            elif action == 2:
                print("Brushia: Thank you for shopping at Bitsclusives!")
                time.sleep(3/2)
                return()
        except ValueError:
            print("Invalid input.")
            time.sleep(1)

def supershinies(data):
    while True:
        iterator = 0
        actions.clear_screen()
        print("Velcia: Haii, welcome to Super-Shinies!!!")
        print(f"Super-Bits: {data.super_bits}")
        print("")
        for x in data.shop_items[1]:
            cost = math.floor(x["cost"] + (5 ** (scaling_mod * x["tier"])))
            print(f"Item #{iterator + 1}. {x["id"]} (Tier: {x["tier"]}) (Cost: {cost})")
            iterator += 1
        print("\n1. Buy item")
        print("2. Back to the menu")
        try:
            action = int(input("Select the number on which task you selected: "))
            if action == 1:
                try: 
                    action = int(input("Velcia: Oh umm which one? (#): "))
                    amnt = input("Velcia: How much? (# or max): ")
                    shop_purchase(action, data, amnt, 2)
                except ValueError:
                    print("Invalid input.")
                    time.sleep(1)
            elif action == 2:
                print("Velcia: Hehe~ Come back soon!")
                time.sleep(3/2)
                return()
        except ValueError:
            print("Invalid input.")
            time.sleep(1)

def imbumentalforge(data):
    while True:
        actions.clear_screen()
        print("Ichor: Greetings. How may my forge be of service today?")
        print(f"Bits {data.bits}")
        print(f"Super-Bits {data.super_bits}")
        print("")
        print(f"Current Imbuement: {data.current_imbuement}")
        print("---------")
        print("1. Imbuement new hex (Cost: 10 Super Bits, 100000000000 Bits)")
        print("2. Forge equipment")
        print("3. View equipment")
        print("4. Back to menu")
        print("---------")
        try:
            action = int(input("Select the number on which task you selected: "))
            if action == 1:
                if data.super_bits >= 10 and data.bits >= 100000000000:
                    data.super_bits -= 10
                    data.bits -= 100000000000 
                    actions.clear_screen()
                    forging(data, "Hex")
                else:
                    if data.bits < 100000000000 and data.super_bits < 10:
                        print(f"Ichor: Sorry my friend. You lack the funds for my services, I'd need {10 - data.super_bits} more Super Bits, and {100000000000 - data.bits} more Bits.")
                        print("Ichor: Maybe Brushia or Velcia can help?")
                    elif data.super_bits >= 10:
                        print(f"Ichor: Sorry my friend. You lack the funds for my services, I'd need {100000000000 - int(data.bits)} more Bits.")
                        print("Ichor: Work on that bit multi!")
                    elif data.bits >= 100000000000:
                        print(f"Ichor: Sorry my friend. You lack the funds for my services, I'd need {10 - data.super_bits} more Super Bits.")
                        print("Ichor: Perhaps some super bit chance upgrades are in order?")
                    time.sleep(3.5)
            elif action == 2:
                while True:
                    actions.clear_screen()
                    print("Ichor: Equipment? My forge is waiting for your command...")
                    print(f"Super Bits: {data.super_bits}")
                    print(f"Molten Bits: {data.molten_bits}")
                    print("\nItem #1 Forge charm (Cost: 5 Molten Bits, 2500 Super Bits)")
                    print("Item #2 Exchange Super Bits to Molten Bits (Cost: 250 Super Bits)\n")
                    print("1. Forge Charm")
                    print("2. Exchange for Molten Bits")
                    print("3. Back to the menu")
                    try:
                        action = int(input("Ichor: So what will it be? "))
                        if action == 1:
                            if data.molten_bits >= 5 and data.super_bits >= 250:
                                forging(data,"Equipment")
                            elif data.molten_bits >= 5:
                                print(f"Ichor: Sorry my friend, but it appears you do not have enough Super Bits. My services require {(50 - data.super_bits)} more of them.")
                                time.sleep(5/2)
                            elif data.super_bits >= 50:
                                print(f"Ichor: My deepest apologies, but it appears you do not have enough Molten Bits. My services require {(5 - data.molten_bits)} more of them.")
                                time.sleep(5/2)
                            else:
                                print(f"Ichor: Oh goodness! It appears you do not have enough Molten Bits or Super Bits! Please come back with {(50 - data.super_bits)} Super and {(5 - data.molten_bits)} Molten Bits .")
                                time.sleep(5/2)
                        elif action == 2:
                            if data.super_bits >= 60:
                                data.super_bits -= 60
                                data.molten_bits += 1
                            else:
                                print(f"Ichor: Sorry my friend, you are lacking funds. I'll require {50 - data.super_bits} more Super Bits.")
                                time.sleep(3/2)
                        else:
                            break
                    except ValueError:
                        print("Invalid Input.")
                        time.sleep(3/2)
                

            elif action == 3:
                iter1 = 0
                target_found = False
                actions.clear_screen()
                for x in imbument_list:
                    for y in imbument_list[iter1]:
                        if y["name"] == data.current_imbuement:
                            print(f"Current Hex: {y["name"]}")
                            print(f"Description: {y["Desc"]}")
                            print(f"Rarity: {y["rarity"]}")
                            target_found = True
                            break
                    iter1 += 1
                iter1 = 0
                for x in equipment_list:
                    try:
                        for y in equipment_list[iter1]:
                            if y["name"] == data.equipment:
                                print(f"\nCurrent Equipment: {y["name"]}")
                                print(f"Description: {y["Desc"]}")
                                print(f"Rarity: {y["rarity"]}\n")
                                target_found = True
                                break
                        iter1 += 1
                    except:
                        pass
                if target_found == False:
                    print("You dont any imbuement or equipment!")
                    print("Buy one from Ichor!")
                    time.sleep(3/2)
                input("Press enter to return...")
            elif action == 4:
                print("Ichor: Thank you for visiting, may luck grace your life.")
                time.sleep(3/2)
                return
        except Exception as e:
            print("Invalid input.")
            time.sleep(2)

def shop_purchase(buy_item, data, buy_amnt, shop):
    if data.shop_items[0][2]["tier"] >= 200 and (buy_item) == 3 and shop == 1:
        print("Brushia: Super-bit chance is already maxed!")
        time.sleep(3/2)
        return
    elif data.shop_items[1][2]["tier"] >= 100 and (buy_item) == 2 and shop == 2:
        print("Velcia: Whoops! That upgrade's all sold out, hehe~")
    try:
        final_cost = 0
        base_cost = data.shop_items[(shop - 1)][(buy_item - 1)]["cost"]
        tier = data.shop_items[(shop - 1)][(buy_item - 1)]["tier"]
        
        if buy_amnt.lower() == "max":
            iterator = 0
            while True:
                if shop == 1 and final_cost > data.bits:
                    final_cost -= math.floor(base_cost + (5 ** (scaling_mod * (tier + iterator))))
                    iterator -= 1
                    break          
                elif shop == 2 and final_cost > data.super_bits:
                    final_cost -= math.floor(base_cost + (5 ** (scaling_mod * (tier + iterator))))
                    iterator -= 1
                    break
                cost = math.floor(base_cost + (5 ** (scaling_mod * (tier + iterator))))
                final_cost += cost
                iterator += 1
            buy_amnt = iterator
        elif buy_amnt.isnumeric() == False:
            print("Invalid input.")
            time.sleep(3/2)
            return
        else:
            buy_amnt = int(buy_amnt)
            for x in range(buy_amnt):
                cost = math.floor(base_cost + (5 ** (scaling_mod * (tier + x))))
                final_cost += cost

    except IndexError:
        print("This item doesn't exist! Check the shop to make sure it exists.")
        time.sleep(1)
        return
    
    if shop == 1 and data.bits >= final_cost:
        pass
    elif shop == 2 and data.super_bits >= final_cost: 
        pass
    else:
        if shop == 1:
            print(f"Brushia: You don't have enough bits! You need {final_cost - int(data.bits)} more!")
            time.sleep(1)
            return
        elif shop == 2:
            print(f"Velcia: Oops! You don't have enough of those, you'd need {final_cost - data.super_bits} more!")
            time.sleep(1)
            return

    if (buy_item - 1) < len(data.shop_items[(shop - 1)]):
        data.shop_items[(shop - 1)][(buy_item - 1)]["tier"] += 1 * buy_amnt
        item_name = data.shop_items[(shop - 1)][(buy_item - 1)]["id"]
        tier_upgrading(data, item_name, shop, final_cost, buy_amnt)
    elif (buy_item - 1) >= len(data.shop_items[shop]):
        print("This item doesn't exist! Check the shop to make sure it exists.")
        time.sleep(1)
    
def tier_upgrading(data, item_name: str, shop: int, final_cost, buy_amnt: int):
    if shop == 1:
        data.bits -= final_cost
    elif shop == 2:
        data.super_bits -= final_cost

    for i in range(buy_amnt + 1):
        if item_name == "Heat Rate":
            data.heat_rate /= 1.75
        elif item_name == "Bit Multi":
            data.bit_multi += 1
        elif item_name == "Super-Bit Chance":
            data.super_bit_chnce += 1
        elif item_name == "Xtra Fuse":
            data.bonus_fuses += 1 
        elif item_name == "Better Fuses": 
            data.fuse_durability += 1 
        elif item_name == "Super-Bit Chance II":
            data.super_bit_chnce += 1

def forging(data, forge_type):
    actions.clear_screen()
    rarity = -1
    if forge_type == "Hex":
        roll = random.randint(0,15)
        if roll == 15:
            print("GLEAM!!~")
            rarity = 4
        elif roll >= 13:
            print("DAZZLE!~")
            rarity = 3
        elif roll >= 9:
            print("SHINE!")
            rarity = 2
        elif roll >= 3:
            print("CLANG!")
            rarity = 1
        else:
            print("CRACK!")
            time.sleep(1)
            print("Your imbument stone cracked under the pressure! Unlucky...")
            time.sleep(3/2)
            data.current_imbuement = "None"
            return
        time.sleep(1)
        rolled_imbuement = random.randint(0, (len(imbument_list[(rarity - 1)]) - 1))
        data.current_imbuement = imbument_list[(rarity - 1)][rolled_imbuement]["name"]
        print(f"Your imbuement stone hexxed you with {imbument_list[(rarity - 1)][rolled_imbuement]["name"]}!")
        print(f"Hex description: {imbument_list[(rarity - 1)][rolled_imbuement]["Desc"]}")
        print(f"Hex Rarity: {imbument_list[(rarity - 1)][rolled_imbuement]["rarity"]}")
        input("\nPress enter to return...")
    elif forge_type == "Equipment":
        roll = random.randint(0,10)
        if roll == 10:
            print("POP!~")
            rarity = 3
        elif roll >= 7:
            print("HISS!")
            rarity = 2
        elif roll >= 4:
            print("BANG!")
            rarity = 1
        else:
            print("BUBBLE")
            time.sleep(1)
            print("The Forge's lava melted your molten bits! Try again...")
            time.sleep(3/2)
            data.equipment = "None"
            return
        time.sleep(1)
        rolled_equipment = random.randint(0, (len(equipment_list[(rarity - 1)]) - 1))
        data.equipment = equipment_list[(rarity - 1)][rolled_equipment]["name"]
        print(f"You forged a {equipment_list[(rarity - 1)][rolled_equipment]["name"]}!")
        print(f"Equipment description: {equipment_list[(rarity - 1)][rolled_equipment]["Desc"]}")
        print(f"Equipment Rarity: {equipment_list[(rarity - 1)][rolled_equipment]["rarity"]}")
        input("\nPress enter to return...")
