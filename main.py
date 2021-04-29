import pandas as pd
import math

import py_osrs_dps.player as p
import py_osrs_dps.enemy as e
import py_osrs_dps.dps as d

# Load NPCs into a DataFrame
# TODO: Put this in enemy.py instead?
npcs = pd.read_csv("npcs/npcs.csv").set_index("NPC")

g1 = p.Gear(weapon="Twisted bow",
            ammo="Dragon arrow",
            style="Ranged rapid",
            cape="Ava's assembler",
            neck="Necklace of anguish")

g2 = p.Gear(weapon="Scythe of vitur",
            style="Slash aggressive",
            head="Neitiznot faceguard",
            cape="Infernal cape",
            neck="Amulet of torture",
            body="Bandos chestplate",
            legs="Bandos tassets",
            hands="Ferocious gloves",
            feet="Primordial boots",
            ring="Berserker ring (i)")

you = p.Player(gear=g1)
also_you = p.Player(gear=g2)
enemy = e.Enemy(npcs.loc["Nylocas Hagios (big)"], scale=5)
d1 = d.DPS(you, enemy)
d2 = d.DPS(also_you, enemy)

print(f"d1.dps: {d1.dps}")
print(f"d2.dps: {d2.dps}")

# Modifying scythe max hit and re-running the calcs gets us a number that's
# kinda close to what the spreadsheet says; will need further testing:
# 
# >>> d2.max_hit
# 48
# >>> d2.max_hit = 48 + int(48/2) + int(48/4)
# >>> d2.max_hit
# 84
# >>> d2.dph = (d2.max_hit * d2.accuracy) / 2
# >>> d2.dph
# 28.463356458024784
# >>> d2.dps = d.calc_dps(d2.dph, g2)
# >>> d2.dps
# 9.487785486008262
#
# Spreadsheet says 9.487855829
