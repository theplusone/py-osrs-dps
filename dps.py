from magic import spells

def calc_max_hit(stats, gear):
    if not gear.style.startswith("magic"):
        s = gear.style.split(" ")[0]
        if (s == "Stab") or (s == "Slash") or (s == "Crush"):
            strength = stats.strength
            equipment_str = gear.bonuses["Strength"]
        else:
            strength = stats.ranged_str
            equipment_str = gear.bonuses["Ranged strength"]
        step1 = strength * (equipment_str + 64)
        step2 = (step1 + 320)/640
        step3 = int(step2) * 1.00 # TODO: s/1.00/whatever gear bonus/
        return int(step3)
    else:
        max_hit = spells[gear.spell]
        if gear.spell.endswith("built-in"):
            M_off = stats.magic_str - 75
            max_hit = max_hit + int(M_off/3)
        bonus = 1 + gear.bonuses["Magic damage"]
        # TODO: Account for other bonuses (salve, slayer, tome of fire)
        return int(max_hit * bonus)

def calc_atk_roll(stats, gear):
    style = gear.style.split(" ")[0]
    atk_bonus = gear.bonuses[style + " attack"]
    if (style == "Stab") or (style == "Slash") or (style == "Crush"):
        step1 = stats.attack * (atk_bonus + 64)
    elif (style == "Ranged"):
        step1 = stats.ranged * (atk_bonus + 64)
    elif (style == "Magic"):
        step1 = stats.magic * (atk_bonus + 64)
    step2 = step1 * 1.00 # TODO: Set bonuses
    return int(step2)

class DPS:
    def __init__(self, you, enemy):
        self.you = you
        self.enemy = enemy
        self.max_hit = calc_max_hit(self.you.stats, self.you.gear)
        self.atk_roll = calc_atk_roll(self.you.stats, self.you.gear)
