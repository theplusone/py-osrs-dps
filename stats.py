class Stats:
    def __init__(self, attack=99, strength=99, defence=99, magic=99,
                 ranged=99, hitpoints=99, prayer=99, ranged_str=99):
        self.attack    = attack
        self.strength  = strength
        self.defence   = defence
        self.magic     = magic
        self.ranged    = ranged
        self.hitpoints = hitpoints
        self.prayer    = prayer
        # "Hidden" stats. According to the DPS spreadsheet, this ranged strength
        # is a separate value from the ranged strength shown in the equipment
        # tab.
        self.ranged_str = ranged_str
