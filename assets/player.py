# Created on 2026-01-03

import time, random, os, math
import assets.actions as actions
import assets.shops as shops

class Player():
    def __init__(self, name="Player"):
        self.shop_items = [[{"tier" : 1, "cost" : 10, "id" : "Heat Rate"}, {"tier" : 1, "cost" : 25, "id" : "Bit Multi"}, {"tier" : 1, "cost" : 1000, "id" : "Super-Bit Chance"}],[{"tier" : 1, "cost" : 5, "id" : "Xtra Fuse"}, {"tier" : 1, "cost" : 15, "id" : "Better Fuses"}, {"tier" : 1, "cost" : 10, "id" : "Super-Bit Chance II"}]]
        self.temp_bonuses = {"bit_B_multi" : 0, "bit_Sp_multi" : 0, "s_bit_multi" : 0, "s_bit_chance" : 0, "s_bit_chanceH" : 0, "heat_divide" : 0, "xtra_fuses" : 0, "heat_max" : 0}
        self.heat = 0
        self.heat_rate = 20 
        self.heat_max = 225
        self.bits = 0
        self.bit_cooldown = 2
        self.bit_multi = 1
        self.prestige = 0
        self.stardust = 0
        self.stardust_mult = 1
        self.super_bits = 0
        self.super_bit_chnce = 0
        self.molten_bits = 0
        self.bonus_fuses = 0
        self.fuse_durability = 0
        self.name = name
        self.current_imbuement = "None"
        self.equipment = "None"
        self.screen = "NULL"
        self.status = "Nominal"
    
    def bit_production(self):
        self.temp_adders()
        self.heat = 0
        fuse_cnt = 1 + self.bonus_fuses + self.temp_bonuses["xtra_fuses"]
        true_heat_max = self.heat_max + self.temp_bonuses["heat_max"]
        if fuse_cnt <= 0:
            fuse_cnt = 1
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
            
            heat_roll = 0
            if (self.heat >= true_heat_max):
                molten_roll = random.randint(0,100)
            elif (self.heat >= (true_heat_max + 50)):
                molten_roll = random.randint(0,25)
            elif (self.heat >= (true_heat_max + 100)):
                molten_roll = random.randint(0,5)
            else:
                heat_roll = random.randint(0, (true_heat_max - int(self.heat)))
            try:
                if self.super_bit_chnce > 0:
                    super_roll = random.randint(0, (100 - int(math.floor((self.super_bit_chnce + self.temp_bonuses["s_bit_chance"]) / 10 + (((self.heat / 10) * self.temp_bonuses["s_bit_chanceH"]))))))
            except:
                super_roll = random.randint(0, 10)


            if (heat_roll == 0): 
                break_roll = random.randint(0, 0 + self.fuse_durability)
                if break_roll == 0:
                    fuse_cnt -= 1
            try:
                if self.status != "Nominal":
                    self.bits += (1 * ((self.bit_multi + self.temp_bonuses["bit_B_multi"]) * ((0.1 / self.bit_cooldown) / 2))) * (self.temp_bonuses["bit_Sp_multi"] + 1)
                    self.heat += 0.1 / (1 + self.temp_bonuses["heat_divide"])
                    time.sleep(0.1) 
                else:
                    self.bits += (1 * (self.bit_multi + self.temp_bonuses["bit_B_multi"])) * (self.temp_bonuses["bit_Sp_multi"] + 1)
                    self.heat += self.heat_rate / (1 + self.temp_bonuses["heat_divide"])
                    time.sleep(self.bit_cooldown)
            except OverflowError:
                pass
            try:
                if super_roll == 0:
                    self.super_bits += 1 * (1 + (self.temp_bonuses["s_bit_multi"]))
            except:
                pass
            try:
                if molten_roll == 0 and self.equipment == "Molten Charm":
                    self.molten_bits += 1
            except:
                pass
            if self.bits < 1e250:
                self.production_HUD(fuse_cnt)
            else:
                self.prestige_HUD()
                return

    def production_HUD(self, fuse_cnt):
        content_lines = [
            "======",
            f"Heat: {math.floor(self.heat)}",
            f"Fuses: {fuse_cnt}",
            f"Status: {self.status}",
            f"Total Bits: {(math.floor(self.bits))}",
            f"Total Super Bits: {(math.floor(self.super_bits))}",
            f"Total Molten Bits: {math.floor(self.molten_bits)}",
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

    def prestige_HUD(self):
        actions.clear_screen()
        print("The glass facade of reality shatters, revealing to you the true beauty of time and space...")
        time.sleep(1)
        if self.prestige == 0:    
            print("No longer held back by the shackles of the living, you confront the god of this universe...")
        else:
            print("No longer wanting to be shackled by your avatar, you seek wisdom from the simulation master...")
        time.sleep(1)
        if self.prestige == 0:
            print("You tremble and shake at the feeling of invisible energy from an unknown source...")
        else:
            print("You feel the comforting presence of someone caring for you...")
        time.sleep(1)
        print("SYSTEM: GR33TINGS PL4Y3R.")
        time.sleep(1)
        if self.prestige == 0:
            print("SYSTEM: W3 H4V3N'T M3T B3 4.")
            time.sleep(1)
            print("SYSTEM: I AM TH3 OWN3R 0F TH3 S!MULATI0N Y0U AR3 EXP3RINCING!")
            time.sleep(3/2)
            print("SYSTEM: MY M3SSAGES SHOULD BE PATCH!NG THROUGH CL3ANER NOW.")
            time.sleep(3/2)
            print("SYSTEM: IT'S GOOD TO SEE THE PROGRAM HAS WORKED!")
            time.sleep(3/2)
            print("SYSTEM: BUT ENOUGH ABOUT THAT, WHAT DO YOU WANT, MY BELOVED TEST SUBJECT?")
        else:
            print("SYSTEM: GOOD T0 SEE YOU AGAIN! NOW, PICK YOUR CHOICE!")
        time.sleep(3)
        shops.rift_station(self)

        
    def display_stats(self):
        print("STATISTICS:")
        print("==========")
        print(f"Username: {self.name}")
        print(f"Bits: {self.bits}")
        print(f"Prestige: {self.prestige}")
        print(f"Bit Cooldown: {self.bit_cooldown} seconds")
        print(f"Heat Rate: {(self.heat_rate)}/cycle")
        print(f"Super-Bits: {self.super_bits}")
        print(f"Super-Bit Chance: {(self.super_bit_chnce) / 10}%")
        print(f"Fuses: {(1 +  self.bonus_fuses) + self.temp_bonuses["xtra_fuses"]}")
        print(f"Fuse Durability: {(self.fuse_durability)}")
        print(f"Current Imbuement: {(self.current_imbuement)}")
        print(f"Current Equipment: {self.equipment}")
        print("-------------")
        print(f"Total Multi: {(self.bit_multi) + (0.1 / self.bit_cooldown)}")
        print(f"Bits per second: {(self.bit_multi) + (1 / self.bit_cooldown)}/sec")
        print("\n")
        input("Press enter to return back...")
    
    def temp_adders(self):
        self.temp_bonuses["heat_divide"] = 0
        self.temp_bonuses["xtra_fuses"] = 0
        self.temp_bonuses["fuse_dura"] = 0
        self.temp_bonuses["bit_B_multi"] = 0
        self.temp_bonuses["bit_Sp_multi"] = 0
        self.temp_bonuses["s_bit_multi"] = 0
        self.temp_bonuses["s_bit_chance"] = 0
        self.temp_bonuses["s_bit_chanceH"] = 0  
    
        # if statement hell 

        if self.current_imbuement == "Deep Freeze":
            self.temp_bonuses["heat_divide"] = 3
        elif self.current_imbuement == "Upgraded Multi":
            self.temp_bonuses["bit_B_multi"] = 2
        elif self.current_imbuement == "Flameborne":
            self.temp_bonuses["s_bit_chanceH"] = 10
        elif self.current_imbuement == "Work Smarter":
            self.temp_bonuses["xtra_fuses"] = 3
        elif self.current_imbuement == "Superior Multi":
            self.temp_bonuses["bit_Sp_multi"] = 1
            self.temp_bonuses["s_bit_multi"] = 1
        elif self.current_imbuement == "Nudge the Scales":
            self.temp_bonuses["s_bit_chance"] = 9
        elif self.current_imbuement == "Omnibus pro Unus et Unus pro Nemine":
            self.temp_bonuses["bit_Sp_multi"] = 1/2
            self.temp_bonuses["xtra_fuses"] = -2
            self.temp_bonuses["s_bit_multi"] = 3
            self.temp_bonuses["s_bit_chance"] = 200
        elif self.current_imbuement == "Natus ex igne et flamma":
            self.temp_bonuses["s_bit_chanceH"] = 25
            self.temp_bonuses["heat_divide"] = -0.5
            self.temp_bonuses["heat_max"] = 100
        
        # part ii (i promise i'll fix this one day)

        if self.equipment == "Super Amulet":
            self.temp_bonuses["s_bit_multi"] += 2
        elif self.equipment == "Fused-Iron Ring":
            self.temp_bonuses["fuse_dura"] += 8
        elif self.equipment == "Molten Charm":
            self.temp_bonuses["heat_max"] += 25