from . import magic
spells = magic.spells

def tbow_max_bonus(max_hit, enemy_stats):
    # Max magic level varies based on location
    magic_cap = 250
    if enemy_stats["Location"] == "Raids":
        magic_cap = 350
    # m = enemy magic level or magic attack, whichever is greater
    m = enemy_stats["Magic level"]
    if enemy_stats["Magic attack"] > m:
        m = enemy_stats["Magic attack"]
    # cap m if necessary
    if m > magic_cap:
        m = magic_cap
    # see wiki article for twisted bow for an easier-to-parse formula
    dmg_pct = 250 + ((10*3*m)/10 - 14)/100 - (3*m/10-140)**2/100
    # bonus has bounds [0,250]
    if dmg_pct < 0:
        dmg_pct = 0
    if dmg_pct > 250:
        dmg_pct = 250
    print(f"damage -> twisted bow -> {dmg_pct/100}")
    return int(max_hit * dmg_pct/100)

def calc_max_hit(stats, gear, size, enemy_stats):
    if not gear.style.startswith("Magic"):
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

        if gear.weapon.name == "Scythe of vitur":
            if size == 2:
                return int(step3) + int(step3/2)
            elif size >= 3:
                return int(step3) + int(step3/2) + int(step3/4)

        if gear.weapon.name == "Twisted bow":
            return tbow_max_bonus(step3, enemy_stats)

        return int(step3)
    else:
        max_hit = spells[gear.spell]
        if gear.spell.endswith("built-in"):
            M_off = stats.magic_str - 75
            max_hit = max_hit + int(M_off/3)
        bonus = 1 + gear.bonuses["Magic damage"]
        # TODO: Account for other bonuses (salve, slayer, tome of fire)
        return int(max_hit * bonus)

def tbow_acc_bonus(atk_roll, enemy_stats):
    # Max magic level varies based on location
    magic_cap = 250
    if enemy_stats["Location"] == "Raids":
        magic_cap = 350
    # m = enemy magic level or magic attack, whichever is greater
    m = enemy_stats["Magic level"]
    if enemy_stats["Magic attack"] > m:
        m = enemy_stats["Magic attack"]
    # cap m if necessary
    if m > magic_cap:
        m = magic_cap
    # see wiki article for twisted bow for an easier-to-parse formula
    acc_pct = 140 + ((10*3*m)/10 - 10)/100 - (3*m/10-100)**2/100
    # bonus has bounds [0,140]
    if acc_pct < 0:
        acc_pct = 0
    if acc_pct > 140:
        acc_pct = 140
    print(f"accuracy -> twisted bow -> {acc_pct/100}")
    return int(atk_roll * acc_pct/100)
    
    
def calc_atk_roll(stats, gear, enemy_stats):
    style = gear.style.split(" ")[0]
    atk_bonus = gear.bonuses[style + " attack"]
    if (style == "Stab") or (style == "Slash") or (style == "Crush"):
        step1 = stats.attack * (atk_bonus + 64)
    elif (style == "Ranged"):
        step1 = stats.ranged * (atk_bonus + 64)
        if gear.weapon.name == "Twisted bow":
            step1 = tbow_acc_bonus(step1, enemy_stats)
    elif (style == "Magic"):
        step1 = stats.magic * (atk_bonus + 64)
    step2 = step1 * 1.00 # TODO: Set bonuses
    return int(step2)

def calc_def_roll(style, stats):
    if style == "Magic":
        defence = stats["Magic level"]
    else:
        defence = stats["Defence level"]
    return int((defence + 9) * (stats[style + " defence"] + 64))

def calc_accuracy(atk_roll, def_roll):
    if atk_roll > def_roll:
        return 1 - (def_roll + 2)/(2 * atk_roll + 1)
    else:
        return atk_roll/(2 * def_roll + 1)

def calc_dps(dph, gear):
    if "rapid" in gear.style:
        gear.bonuses["Speed"] = gear.bonuses["Speed"] - 1
    speed_in_seconds = gear.bonuses["Speed"] * 0.6
    return dph / speed_in_seconds
