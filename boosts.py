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
