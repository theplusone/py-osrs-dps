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
