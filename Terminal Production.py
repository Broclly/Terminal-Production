# Created on 2026-01-03

import time, random, os, math
import assets.player as player, assets.actions as actions, assets.shop as shop

user = player.Player()
build_ver = 0.2


def welcome():
    user.screen = "start"
    print(f"Welcome to Terminal Production! (v{build_ver})")
    input("Press enter to start")
    

def main_menu():
    actions.clear_screen()
    user.screen = "actions1"
    while True:
        actions.clear_screen()
        print("1. New")
        print("2. Load Game")
        print("3. Quit")
        try: 
            temp = int(input("Select the number on which task you selected: "))
            if temp == 1:
                user.name = input("Enter your username: ")
                game_play()
            elif temp == 2:
                file_to_load = input("Enter your username: ")
                load_check = actions.load_game(file_to_load, user)
                if load_check != 0:
                    actions.load_shop(file_to_load, user)
                    game_play()
                else:
                    print("This file does not exist! Make sure you are trying to load an existing file.")
                    print("Do not include the .json file extension")
                    print("Do not try to load the -shop.json file")
                    time.sleep(3)
                    actions.clear_screen()
            elif temp == 3:
                quit()
        except ValueError:
            print("Invalid input.")
            time.sleep(3/2)

def game_play():
    while True: 
        actions.clear_screen()
        print("Username: " + user.name)
        print("Bits: " + str(math.floor(user.bits)))
        print("Super Bits: " +str(math.floor(user.super_bits)))
        print("========")
        print("1. Produce Bits")
        print("2. Shop")
        print("3. Save")
        print("4. Back to menu")
        try:
            temp = int(input("Select the number on which task you selected: "))
            if temp == 1:
                actions.clear_screen()
                user.bit_production()
            elif temp == 2:
                actions.load_shop(user.name,user)
                shop.shop_menu(user)
                actions.save_shop(user)
                actions.save_game(user)
                actions.load_game(user.name,user)
                actions.clear_screen()
            elif temp == 3:
                actions.save_game(user)
                actions.save_shop(user)
                actions.load_game(user.name,user) # refreshes data
                actions.clear_screen()
            elif temp == 4:
                return
            else:
                print("Invalid input")
                time.sleep(3/2)
        except ValueError:
            print("Invalid input.")
            time.sleep(3/2)


welcome()
main_menu()