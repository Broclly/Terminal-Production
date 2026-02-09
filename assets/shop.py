# Created on 2026-02-05

import math, time, os

def shop_menu(data):
    while True:
        os.system(('clear'))
        print("Welcome to the Bitsclusives!")
        print("Bits: " + str(math.floor(data.bits)))
        print("")
        iterator = 0
        for x in data.shop_items:
            cost = math.floor(x["cost"] + (5 ** (0.25 * x["tier"])))
            print(f"Item #{iterator + 1}. {x["id"]} (Tier: {x["tier"]}) (Cost: {cost})")
            iterator += 1
        print("\n1. Buy item")
        print("2. Back to the menu")
        try:
            action = int(input("Select the number on which task you selected: "))
            if action == 1:
                try: 
                    action = int(input("Select which item would you like to buy: "))
                    amnt = int(input("Select how many you would like to buy: "))
                    shop_purchase(action, data, amnt)
                except ValueError:
                    print("Invalid input.")
                    time.sleep(1)
            elif action == 2:
                print("Thank you for shopping at Bitsclusives!")
                time.sleep(3/2)
                return()
        except ValueError:
            print("Invalid input.")
            time.sleep(1)

def shop_purchase(buy_item, data, buy_amnt):
    try:
        final_cost = 0
        base_cost = data.shop_items[(buy_item - 1)]["cost"]
        tier = data.shop_items[(buy_item - 1)]["tier"]
        for x in range(buy_amnt):
            cost = math.floor(base_cost + (5 ** (0.25 * (tier + x))))
            print(cost)
            final_cost += cost
            print(final_cost)
        input("")

    except IndexError:
        print("This item doesn't exist! Check the shop to make sure it exists.")
        time.sleep(1)
        return

    if data.bits >= final_cost and (buy_item - 1) < len(data.shop_items):
        data.shop_items[(buy_item - 1)]["tier"] += 1 * buy_amnt
        data.bits -= final_cost
        if buy_item == 1:
            data.heat_rate /= (1.75 * buy_amnt)
        elif buy_item == 2:
            data.bit_multi += (1 * buy_amnt)
    elif (buy_item - 1) >= len(data.shop_items):
        print("This item doesn't exist! Check the shop to make sure it exists.")
        time.sleep(1)
    else: 
        print(f"You don't have enough bits! You need {final_cost - data.bits} more!")
        time.sleep(1)