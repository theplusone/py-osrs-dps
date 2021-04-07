from magic import spells

def calc_max_hit(stats, gear):
    """
    Given stats and gear, calculate the max hit.
    """
    if not gear.style.startswith("magic"):
        s = gear.style.split(" ")[0]
        if (s == "stab") or (s == "slash") or (s == "crush"):
            strength = stats.strength
            equipment_str = gear.bonuses["Strength"]
        else:
            strength = stats.ranged_str
            equipment_str = gear.bonuses["Ranged strength"]
        step1 = strength * (equipment_str + 64)
        step2 = (step1 + 320)/640
        step3 = int(step2) * 1.00 # TODO: s/1.00/whatever gear bonus
        return int(step3)
    else:
        max_hit = spells[gear.spell]
        if gear.spell.endswith("built-in"):
            M_off = stats.magic_str - 75
            max_hit = max_hit + int(M_off/3)
        bonus = 1 + gear.bonuses["Magic damage"]
        # TODO: Account for other bonuses (salve, slayer, tome of fire)
        return int(max_hit * bonus)

class DPS:
    def __init__(self, you, enemy):
        self.you = you
        self.enemy = enemy
        self.max_hit = calc_max_hit(self.you.stats, self.you.gear)
