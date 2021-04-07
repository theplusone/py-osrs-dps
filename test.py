import pandas as pd
import math
import player as p
from dps import DPS

# Load NPCs into a DataFrame
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
enemy = npcs.loc["Muttadiles (small)"]
d = DPS(you, enemy)

