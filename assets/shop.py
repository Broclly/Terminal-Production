# Created on 2026-02-05

import math, time, os

from assets import actions

scaling_mod = 0.31

def shop_menu(data):
    while True:
        actions.clear_screen()
        print("Which shop will you go to?")
        print("1. Bitsclusives")
        print("2. Super-Shinies")
        print("3. Imbumental Forge")
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
            pass

def bitsclusives(data):
    while True:
        actions.clear_screen()
        print("Brushia: Welcome to the Bitsclusives!")
        print("Bits: " + str(math.floor(data.bits)))
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
                    action = int(input("Which item would you like? (#): "))
                    amnt = int(input("How many of those? (#): "))
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
                    action = int(input("Oh umm which one? (#): "))
                    amnt = int(input("How much? (#): "))
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

def shop_purchase(buy_item, data, buy_amnt, shop):
    if data.shop_items[0][2]["tier"] == 50 and (buy_item) == 3:
        print("Brushia: Super-bit chance is already maxed!")
        time.sleep(3/2)
        return
    try:
        final_cost = 0
        base_cost = data.shop_items[(shop - 1)][(buy_item - 1)]["cost"]
        tier = data.shop_items[(shop - 1)][(buy_item - 1)]["tier"]
        for x in range(buy_amnt):
            cost = math.floor(base_cost + (5 ** (scaling_mod * (tier + x))))
            print(cost)
            final_cost += cost

    except IndexError:
        print("This item doesn't exist! Check the shop to make sure it exists.")
        time.sleep(1)
        return

    if data.bits >= final_cost and (buy_item - 1) < len(data.shop_items):
        input("2")
        data.shop_items[(shop - 1)][(buy_item - 1)]["tier"] += 1 * buy_amnt
        input("3")
        print((shop - 1))
        print((buy_item - 1))
        item_name = data.shop_items[(shop - 1)][(buy_item - 1)]["id"]
        input("")

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
            data.fuse_cnt += 1
    elif (buy_item - 1) >= len(data.shop_items):
        print("This item doesn't exist! Check the shop to make sure it exists.")
        time.sleep(1)
    else: 
        if shop == 1:
            print(f"Brushia: You don't have enough bits! You need {final_cost - data.bits} more!")
        elif shop == 2:
            print(f"Velcia: Oops! You don't have enough of those, you'd need {final_cost - data.super_bits} more!")
        time.sleep(1)