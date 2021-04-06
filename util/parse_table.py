#!/usr/bin/env python3

"""
Python script to parse the slot tables from the OSRS wiki.
e.g. https://oldschool.runescape.wiki/w/Weapon_slot_table

./parse_table.py https://oldschool.runescape.wiki/w/Weapon_slot_table > out.csv
"""

import sys
import requests as r
import pandas as pd

# Get the slot table from the given url
response = r.get(sys.argv[1]) 
items = pd.read_html(response.text)[-1]

# Get rid of the thumbnail and F2P/P2P columns, fix column names. Names are
# taken from wiki mouseover for the header icons.
items = items.drop(columns=["Unnamed: 0", "Unnamed: 2"])
columns = ["Name", "Stab attack", "Slash attack", "Crush attack",
           "Magic attack", "Ranged attack", "Stab defence", "Slash defence",
           "Crush defence", "Magic defence", "Ranged defence", "Strength",
           "Ranged strength", "Magic damage", "Prayer", "Speed"]
items.columns = columns

# Fix magic damage column (e.g. "+2%" -> 0.02)
items["Magic damage"] = items["Magic damage"].apply(
    lambda x: float(x.replace("%", ""))/100)

# Output
print(items.to_csv(index=False))
