# Created on 2026-02-05

import math, time, os, random

from assets import actions

scaling_mod = 0.31
imbument_list = [{"name" : "Deep Freeze", "Desc" : "Divides heat by 3", "rarity" : 1}, {"name" : "Work Smarter", "Desc" : "Increases fuse count by +3", "rarity" : 2}, {"name" : "Superior Multi", "Desc" : "2x Super Bits, +3x Bit Multi", "rarity" : 3}]

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
        print(f"Bits: {data.bits}")
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
                    amnt = int(input("Brushia: How many of those? (#): "))
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
                    amnt = int(input("Velcia: How much? (#): "))
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
        print("1. Forge new hex (Cost: 10 Super Bits, 100000000000 Bits)")
        print("2. View current hex")
        print("3. Back to menu")
        print("---------")
        try:
            action = int(input("Select the number on which task you selected: "))
            if action == 1:
                if data.super_bits >= 10 and data.bits >= 100000000000:
                    data.super_bits -= 10
                    data.bits -= 100000000000 
                    actions.clear_screen()
                    forging(data)
                else:
                    if data.bits < 100000000000 and data.super_bits < 10:
                        print(f"Ichor: Sorry my friend. You lack the funds for my services, I'd need {10 - data.super_bits} more Super Bits, and {100000000000 - data.bits} more Bits.")
                        print("Ichor: Maybe Brushia or Velcia can help?")
                    elif data.super_bits > 10:
                        print(f"Ichor: Sorry my friend. You lack the funds for my services, I'd need {100000000000 - data.bits} more Bits.")
                        print("Ichor: Work on that bit multi!")
                    elif data.bits > 100000000000:
                        print(f"Ichor: Sorry my friend. You lack the funds for my services, I'd need {10 - data.super_bits} more Super Bits.")
                        print("Ichor: Perhaps some super bit chance upgrades are in order?")
                    time.sleep(3.5)
            elif action == 2:
                iterator = 1
                actions.clear_screen()
                for x in imbument_list:
                    if x["name"] == data.current_imbuement:
                        print(f"Current hex: {x["name"]}")
                        print(f"Description: {x["Desc"]}")
                        input("\nPress enter to return...")
                        break
                    elif len(imbument_list) == iterator:
                        print("You dont have any imbuements!")
                        print("Talk to Ichor about forging them.")
                        time.sleep(3/2)
                    iterator += 1
            elif action == 3:
                print("Ichor: Thank you for visiting, may luck grace your life.")
                time.sleep(3/2)
                return
        except:
            print("Invalid input.")

def shop_purchase(buy_item, data, buy_amnt, shop):
    if data.shop_items[0][2]["tier"] >= 100 and (buy_item) == 3 and shop == 1:
        print("Brushia: Super-bit chance is already maxed!")
        time.sleep(3/2)
        return
    elif data.shop_items[1][2]["tier"] >= 100 and (buy_item) == 2 and shop == 2:
        print("Velcia: Whoops! That upgrade's all sold out, hehe~")
    try:
        final_cost = 0
        base_cost = data.shop_items[(shop - 1)][(buy_item - 1)]["cost"]
        tier = data.shop_items[(shop - 1)][(buy_item - 1)]["tier"]
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
            print(f"Brushia: You don't have enough bits! You need {final_cost - data.bits} more!")
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

    if item_name == "Heat Rate":
        data.heat_rate /= (1.75 * buy_amnt)
    elif item_name == "Bit Multi":
        data.bit_multi += (1 * buy_amnt)
    elif item_name == "Super-Bit Chance":
        data.super_bit_chnce += (1 * buy_amnt)
    elif item_name == "Xtra Fuse":
        data.bonus_fuses += (1 * buy_amnt)
    elif item_name == "Better Fuses": 
        data.fuse_durability += (1 * buy_amnt)
    elif item_name == "Super-Bit Chance II":
        data.super_bit_chnce += 1

def forging(data):
    roll = random.randint(0,10)
    if roll == 10:
        print("DAZZLE!~")
        rarity = 3
    elif roll >= 7:
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
    data.current_imbuement = imbument_list[(rarity - 1)]["name"]
    print(f"Your imbuement stone hexxed you with {imbument_list[(rarity - 1)]["name"]}!")
    print(f"Hex description: {imbument_list[(rarity - 1)]["Desc"]}")
    input("\nPress enter to return...")
    return