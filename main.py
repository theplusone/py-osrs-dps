import pandas as pd
import math

import py_osrs_dps.player as p
import py_osrs_dps.enemy as e
import py_osrs_dps.dps as d

# Load NPCs into a DataFrame
# TODO: Put this in enemy.py instead?
npcs = pd.read_csv("npcs/npcs.csv").set_index("NPC")

g = p.Gear(weapon ="Trident of the swamp",
           style  ="Magic accurate",
           spell  ="Swamp built-in",
           head   ="Neitiznot faceguard",
           cape   ="Imbued saradomin cape",
           neck   ="Occult necklace",
           body   ="Ahrim's robetop",
           legs   ="Ahrim's robeskirt",
           hands  ="Tormented bracelet")

you = p.Player(gear=g)
enemy = e.Enemy(npcs.loc["Muttadiles (small)"], scale=5)
d = d.DPS(you, enemy)

