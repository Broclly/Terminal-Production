# Created on 2026-01-03

import time, random, os, math
import assets.actions as actions

class Player():
    def __init__(self, name="Player"):
        self.shop_items = [[{"tier" : 1, "cost" : 10, "id" : "Heat Rate"}, {"tier" : 1, "cost" : 25, "id" : "Bit Multi"}, {"tier" : 1, "cost" : 1000, "id" : "Super-Bit Chance"}],[{"tier" : 1, "cost" : 5, "id" : "Xtra Fuse"}, {"tier" : 1, "cost" : 15, "id" : "Better Fuses"}, {"tier" : 1, "cost" : 10, "id" : "Super-Bit Chance II"}]]
        self.temp_bonuses = {"bit_multi" : 0, "s_bit_multi" : 0, "heat_divide" : 0, "xtra_fuses" : 0}
        self.heat = 0
        self.heat_rate = 20 
        self.heat_max = 100
        self.bits = 0
        self.bit_cooldown = 2
        self.bit_multi = 1
        self.super_bits = 0
        self.super_bit_chnce = 0
        self.bonus_fuses = 0
        self.fuse_durability = 0
        self.name = name
        self.current_imbuement = "None"
        self.screen = "NULL"
        self.status = "Nominal"
    
    def bit_production(self):
        input((int(math.floor(self.super_bit_chnce / 10))))
        input(self.fuse_durability)
        self.temp_adders()
        self.heat = 0
        fuse_cnt = 1 + self.bonus_fuses + self.temp_bonuses["xtra_fuses"]
        if self.bit_cooldown < 0.00000000001:
            self.status = ">>>> PERMACHILL <<<<"
        elif self.bit_cooldown < 0.0000001:
            self.status = ">>> HYPERFROST <<<"
        elif self.bit_cooldown < 0.0001:
            self.status = ">> FRIGID <<"
        elif self.bit_cooldown < 0.1:
            self.status = "> SUPERCOOLED <"
        else:
            self.status = "Nominal"
        while True:
            self.production_HUD(fuse_cnt)
            if fuse_cnt == 0:
                self.status = "!!! ALL FUSES BLOWN !!!"
                self.production_HUD(fuse_cnt)
                time.sleep(5/2)
                actions.clear_screen()
                return
            if (self.heat >= 100):
                heat_roll = 0
            else:
                heat_roll = random.randint(0, (self.heat_max - int(self.heat)))
                try:
                    if self.super_bit_chnce > 0:
                        super_roll = random.randint(0, (100 - int(math.floor(self.super_bit_chnce / 10))))
                except:
                    super_roll = random.randint(0, 10)
            if (heat_roll == 0): 
                break_roll = random.randint(0, 0 + self.fuse_durability)
                if break_roll == 0:
                    fuse_cnt -= 1
            if self.status != "Nominal":
                self.bits += 1 * ((self.bit_multi + self.temp_bonuses["bit_multi"]) * ((0.1 / self.bit_cooldown) / 2) )
                self.heat += 0.1 / 1 + self.temp_bonuses["heat_divide"]
                time.sleep(0.1) 
            else: 
                self.bits += 1 * (self.bit_multi + self.temp_bonuses["bit_multi"])
                self.heat += self.heat_rate / 1 + self.temp_bonuses["heat_divide"]
                time.sleep(self.bit_cooldown)
            try:
                if super_roll == 0:
                    self.super_bits += 1 * (1 + (self.temp_bonuses["s_bit_multi"]))
            except:
                pass
            self.production_HUD(fuse_cnt)

    def production_HUD(self, fuse_cnt):
        content_lines = [
            "======",
            f"Heat: {math.floor(self.heat)}",
            f"Fuses: {fuse_cnt}",
            f"Status: {self.status}",
            f"Total Bits: {math.floor(self.bits)}",
            f"Total Super Bits: {math.floor(self.super_bits)}",
            "====="
        ]

        total_lines = 0
        terminal_width = os.get_terminal_size().columns 

        for line in content_lines:
            total_lines += math.ceil(len(line) / terminal_width)
        else:
            for line in content_lines:
                print(f"\033[2K{line}", flush=True)
    
        print(f"\033[{total_lines}A", end='') 

    def display_stats(self):
        print("STATISTICS:")
        print("==========")
        print(f"Username: {self.name}")
        print(f"Bits: {self.bits}")
        print(f"Bit Cooldown: {self.bit_cooldown} seconds")
        print(f"Heat Rate: {(self.heat_rate)}/cycle")
        print(f"Super-Bits: {self.super_bits}")
        print(f"Super-Bit Chance: {(self.super_bit_chnce) / 10}%")
        print(f"Fuses: {(1 + self.bonus_fuses)}")
        print(f"Fuse Durability: {(self.fuse_durability)}")
        print(f"Current Imbuement: {(self.current_imbuement)}")
        print("-------------")
        print(f"Total Multi: {(self.bit_multi) + (0.1 / self.bit_cooldown)}")
        print(f"Bits per second: {(self.bit_multi) + (1 / self.bit_cooldown)}/sec")
        print("\n")
        input("Press enter to return back...")
    
    def temp_adders(self):
        for key, value in self.temp_bonuses.items():
            value = 0
        if self.current_imbuement == "Deep Freeze":
            self.temp_bonuses["heat_divide"] = 3
        elif self.current_imbuement == "Work Smarter":
            self.temp_bonuses["xtra_fuses"] = 3
        elif self.current_imbuement == "Superior Multi":
            self.temp_bonuses["bit_multi"] = 3
            self.temp_bonuses["s_bit_multi"] = 1