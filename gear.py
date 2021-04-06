import pandas as pd

# Load all wieldable items into a singular DataFrame
slot_list = ["1h", "2h", "ammo", "body", "cape", "feet", "hands", "head",
             "legs", "neck", "ring", "shield"]
items = pd.DataFrame()
for slot in slot_list:
    items = items.append(pd.read_csv(f"items/{slot}.csv"), ignore_index=True)
items = items.set_index("Name")
        
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
                 ring=None, style=None):
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
        self.style  = style
