"""
Raid helper functions to scale stats. Makes enemy.py a bit less messy.
"""

def cox_scale_hp(name, hp, scale):
    if "Olm" in name:
        hp = int(hp + (hp * scale))
    elif name == "Guardian":
        # TODO: Don't assume 99 mining
        hp = int(hp * (1 + int(scale / 2))) + (99 * scale)
    else:
        hp = int(hp * (1 + int(scale / 2)))
        
    if "CM" in name:
        hp = hp * 1.5
        
    return hp

def cox_scale_def(name, defence, scale):
    d = int(defence * (1 + (0.01 * (scale - 1))))

    if "Tekton CM" in name:
        return d * 1.2
    elif "CM" in name:
        return d * 1.5
    return d

def cox_scale_magic(name, magic, scale):
    m = int(magic * (1 + (0.07 * (1 + int(scale/5))) + 0.01 * (scale - 1)))

    if "Tekton CM" in name:
        return m * 1.2
    elif "CM" in name:
        return m * 1.5
    return m

def tob_scale_hp(hp, scale):
    if scale == 5:
        return hp
    elif scale == 4:
        return int(hp * 0.875)
    else:
        return int(hp * 0.75)

def scale_stats(stats, scale):
    """
    Applies stat scaling if the enemy is a raids monster.
    """
    # TODO: Rename "Raids" in .csv to "CoX" and rename Theatre to "ToB"
    stats = stats.copy(deep=True) # For suppressing SettingWithCopyWarning
    name = stats.name
    location = stats["Location"]
    
    if (scale == 1) or (location not in ["Raids", "Theatre of Blood"]):
        return stats
    
    if location == "Raids":
        stats["Hitpoints"] = cox_scale_hp(name, stats["Hitpoints"], scale)
        stats["Defence level"] = cox_scale_def(name, stats["Defence level"],
                                               scale)
        stats["Magic level"] = cox_scale_magic(name, stats["Magic level"],
                                               scale)
    elif location == "Theatre of Blood":
        stats["Hitpoints"] = tob_scale_hp(stats["Hitpoints"], scale)

    return stats
