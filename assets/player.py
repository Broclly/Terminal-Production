# Created on 2026-01-03

import time, random, os, math
import assets.actions as actions

class Player():
    def __init__(self, name="Player"):
        self.shop_items = [{"tier" : 1, "cost" : 10, "id" : "Heat Rate"}, {"tier" : 1, "cost" : 25, "id" : "Bit Multi"}]
        self.heat = 0
        self.heat_rate = 20 
        self.heat_max = 100
        self.bits = 0
        self.bit_cooldown = 2
        self.bit_multi = 1
        self.name = name
        self.screen = "NULL"
        self.status = "Nominal"
    
    def bit_production(self):
        self.screen = "prod"
        self.heat = 0
        if self.bit_cooldown < 0.0001:
            self.status = ">>> HYPERFROST <<<"
        elif self.bit_cooldown < 0.01:
            self.status = ">> FRIGID <<"
        elif self.bit_cooldown < 0.1:
            self.status = "> SUPERCOOLED <"
        else:
            self.status = "Nominal"
        while True:
            if (self.heat >= 100):
                heat_roll = 0
            else:
                heat_roll = random.randint(0, (self.heat_max - int(self.heat)))
            if (heat_roll == 0):
                self.status = "!! FUSE BLOWN !!"
                self.production_HUD()
                time.sleep(3)
                self.screen == "actions2"
                actions.clear_screen()
                actions.save_game(self)
                return
            if self.status != "Nominal":
                self.bits += 1 * (self.bit_multi * ((0.1 / self.bit_cooldown) / 2))
                self.heat += 0.1
                time.sleep(0.1) 
            else: 
                self.bits += 1 * self.bit_multi
                self.heat += self.heat_rate
                time.sleep(self.bit_cooldown) 
            self.production_HUD()

    def production_HUD(self):
        content_lines = [
            "======",
            f"Heat: {math.floor(self.heat)}",
            f"Status: {self.status}",
            f"Total Bits {math.floor(self.bits)}",
            "====="
        ]

        total_lines = 0
        terminal_width = os.get_terminal_size().columns 

        for line in content_lines:
            total_lines += math.ceil(len(line) / terminal_width)

        for line in content_lines:
            print(f"\033[2K{line}", flush=True)
    
        print(f"\033[{total_lines}A", end='') 