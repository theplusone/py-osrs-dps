import pandas as pd
import math
import player as p

# Load NPCs into a DataFrame
npcs = pd.read_csv("npcs/npcs.csv").set_index("NPC")

g = p.Gear(weapon="Sanguinesti staff#Charged",
           style="magic accurate",
           head="Ancestral hat",
           cape="Imbued saradomin cape#Normal",
           neck="Occult necklace",
           body="Ancestral robe top",
           legs="Ancestral robe bottom",
           shield="Arcane spirit shield",
           hands="Tormented bracelet")

you = p.Player(gear=g)

assert math.isclose(you.gear.bonuses["Magic damage"], 0.23)
assert you.gear.bonuses["Magic attack"] == 151
