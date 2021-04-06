import pandas as pd
import math

# Load all wieldable items into a singular DataFrame
slot_list = ["1h", "2h", "ammo", "body", "cape", "feet", "hands", "head",
             "legs", "neck", "ring", "shield"]
items = pd.DataFrame()
for slot in slot_list:
    items = items.append(pd.read_csv(f"items/{slot}.csv"), ignore_index=True)
items = items.set_index("Name")

# Load NPCs into a DataFrame
npcs = pd.read_csv("npcs/npcs.csv").set_index("NPC")

# TODO: Put these all in separate files eventually, but just messing around for
# now

class Stats:
    def __init__(self, attack=99, strength=99, defence=99, magic=99,
                 ranged=99, hitpoints=99, prayer=99):
        self.attack    = attack
        self.strength  = strength
        self.defence   = defence
        self.magic     = magic
        self.ranged    = ranged
        self.hitpoints = hitpoints
        self.prayer    = prayer
        
class Gear:
    bonuses = pd.Series(data=0, index=items.columns)
    def find_item(self, item):
        if item:
            found_item = items.loc[item]
            self.bonuses = self.bonuses.add(found_item, fill_value=0)
            return found_item
        else:
            return None
    def __init__(self, weapon=None, ammo=None, head=None, cape=None, neck=None,
                 body=None, legs=None, shield=None, hands=None, feet=None,
                 ring=None):
        self.weapon = self.find_item(weapon)
        self.ammo   = self.find_item(ammo)
        self.head   = self.find_item(head)
        self.cape   = self.find_item(cape)
        self.neck   = self.find_item(neck)
        self.body   = self.find_item(body)
        self.legs   = self.find_item(legs)
        self.shield = self.find_item(shield)
        self.hands  = self.find_item(hands)
        self.feet   = self.find_item(feet)
        self.ring   = self.find_item(ring)

class Prayers:
    allowed_melee  = ["Piety", "Chivalry", "15%", "10%", "5%"]
    allowed_magic  = ["Augury", "15%", "10%", "5%"]
    allowed_ranged = ["Rigour", "15%", "10%", "5%"]
    def is_allowed(self, prayer, prayer_list):
        if (prayer in prayer_list) or (prayer is None):
            return prayer
        else:
            raise ValueError(f"{prayer} not found in {prayer_list}")
    def __init__(self, melee="Piety", magic="Augury", ranged="Rigour"):
        self.melee  = self.is_allowed(melee,  self.allowed_melee)
        self.magic  = self.is_allowed(magic,  self.allowed_magic)
        self.ranged = self.is_allowed(ranged, self.allowed_ranged)

class Boosts:
    # I know there's more boosts than these, but I'm just worried about these
    # for now
    allowed_melee  = ["Super combat", "Overload (+)"]
    allowed_magic  = ["Imbued heart", "Overload (+)"]
    allowed_ranged = ["Ranging", "Overload (+)"]
    def is_allowed(self, boost, boost_list):
        if (boost in boost_list) or (boost is None):
            return boost
        else:
            raise ValueError(f"{boost} not found in {boost_list}")
    def __init__(self, melee="Overload (+)", magic="Overload (+)",
                 ranged="Overload (+)"):
        self.melee  = self.is_allowed(melee,  self.allowed_melee)
        self.magic  = self.is_allowed(magic,  self.allowed_magic)
        self.ranged = self.is_allowed(ranged, self.allowed_ranged)

class Player:
    def __init__(self, stats=Stats(), gear=Gear(), prayers=Prayers(),
                 boosts=Boosts()):
        self.stats   = stats
        self.gear    = gear
        self.prayers = prayers
        self.boosts  = boosts

g = Gear(weapon="Sanguinesti staff#Charged",
         head="Ancestral hat",
         cape="Imbued saradomin cape#Normal",
         neck="Occult necklace",
         body="Ancestral robe top",
         legs="Ancestral robe bottom",
         shield="Arcane spirit shield",
         hands="Tormented bracelet")

p = Player(gear=g)

assert math.isclose(p.gear.bonuses["Magic damage"], 0.23)
assert p.gear.bonuses["Magic attack"] == 151
