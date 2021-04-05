#!/usr/bin/env bash

# Dumb bash script to run ./parse_tables.py against all slots.
# Given the relative directory output, it'd be ideal to run this in the util/
# directory.

echo "Ammo slot..."
./parse_table.py https://oldschool.runescape.wiki/w/Ammunition_slot_table \
                  > ../items/ammo.csv

echo "Body slot..."
./parse_table.py https://oldschool.runescape.wiki/w/Body_slot_table \
                  > ../items/body.csv

echo "Cape slot..."
./parse_table.py https://oldschool.runescape.wiki/w/Cape_slot_table \
                  > ../items/cape.csv

echo "Feet slot..."
./parse_table.py https://oldschool.runescape.wiki/w/Feet_slot_table \
                  > ../items/feet.csv

echo "Hands slot..."
./parse_table.py https://oldschool.runescape.wiki/w/Hands_slot_table \
                  > ../items/hands.csv

echo "Head slot..."
./parse_table.py https://oldschool.runescape.wiki/w/Head_slot_table \
                  > ../items/head.csv

echo "Legs slot..."
./parse_table.py https://oldschool.runescape.wiki/w/Legs_slot_table \
                  > ../items/legs.csv

echo "Neck slot..."
./parse_table.py https://oldschool.runescape.wiki/w/Neck_slot_table \
                  > ../items/neck.csv

echo "Ring slot..."
./parse_table.py https://oldschool.runescape.wiki/w/Ring_slot_table \
                  > ../items/ring.csv

echo "Shield slot..."
./parse_table.py https://oldschool.runescape.wiki/w/Shield_slot_table \
                  > ../items/shield.csv

echo "Two-handed slot..."
./parse_table.py https://oldschool.runescape.wiki/w/Two-handed_slot_table \
                  > ../items/2h.csv

echo "One-handed slot..."
./parse_table.py https://oldschool.runescape.wiki/w/Weapon_slot_table \
                  > ../items/1h.csv
