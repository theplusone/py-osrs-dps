class Stats:
    def __init__(self, attack=99, strength=99, defence=99, magic=99,
                 ranged=99, hitpoints=99, prayer=99, ranged_str=None,
                 magic_str=None):
        self.attack    = attack
        self.strength  = strength
        self.defence   = defence
        self.magic     = magic
        self.ranged    = ranged
        self.hitpoints = hitpoints
        self.prayer    = prayer
        # "Hidden" stats.
        if not ranged_str:
            self.ranged_str = ranged
        else:
            self.ranged_str = ranged_str
        if not magic_str:
            self.magic_str = magic
        else:
            self.magic_str = magic_str
