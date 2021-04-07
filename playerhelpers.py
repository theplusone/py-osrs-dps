# Helper functions for player.py

from stats import Stats

prayer_coeff = {
    "Attack":     {"Piety": 1.20, "Chivalry": 1.15,
                   "15%": 1.15, "10%": 1.10, "5%": 1.05, "None": 1.00},
    "Strength":   {"Piety": 1.23, "Chivalry": 1.18,
                   "15%": 1.15, "10%": 1.10, "5%": 1.05, "None": 1.00},
    "Defence":    {"Piety": 1.25, "Chivalry": 1.20,
                   "15%": 1.15, "10%": 1.10, "5%": 1.05, "None": 1.00},
    "Ranged (a)": {"Rigour": 1.20,
                   "15%": 1.15, "10%": 1.10, "5%": 1.05, "None": 1.00},
    "Ranged (s)": {"Rigour": 1.23,
                   "15%": 1.15, "10%": 1.10, "5%": 1.05, "None": 1.00},
    "Magic":      {"Augury": 1.25,
                   "15%": 1.15, "10%": 1.10, "5%": 1.05, "None": 1.00}
    }

boost_coeff = {
    "Super combat": 1.15,
    "Overload (+)": 1.16,
    "Ranging":      1.10,
    "None":         1.00
}

boost_flat = {
    "Super combat": 5,
    "Overload (+)": 6,
    "Ranging":      4,
    "None":         0
}

def apply_stat_boosts(stats, prayer, boost):
    """
    Given base stats, active prayers, and active potions, calculate the
    effective stat level.
    """
    A, S, D, Ra, Rs, M, Ms = (stats.attack, stats.strength, stats.defence,
                              stats.ranged, stats.ranged_str, stats.magic,
                              stats.magic_str)
    p1, p2, p3 = (prayer.melee, prayer.ranged, prayer.magic)
    b1, b2, b3 = (boost.melee, boost.ranged, boost.magic)
    A  = int((int(A * boost_coeff[b1]) + boost_flat[b1])
             * prayer_coeff["Attack"][p1])
    S  = int((int(S * boost_coeff[b1]) + boost_flat[b1])
             * prayer_coeff["Strength"][p1])
    D  = int((int(D * boost_coeff[b1]) + boost_flat[b1])
             * prayer_coeff["Defence"][p1])
    Ra = int((int(Ra * boost_coeff[b2]) + boost_flat[b2])
             * prayer_coeff["Ranged (a)"][p2])
    Rs = int((int(Rs * boost_coeff[b2]) + boost_flat[b2])
             * prayer_coeff["Ranged (s)"][p2])
    M  = int((int(M * boost_coeff[b3]) + boost_flat[b3])
             * prayer_coeff["Magic"][p3])
    # Magic prayers only affect magic accuracy, so prayer_coeff's ignored here
    Ms = int(int(Ms * boost_coeff[b3]) + boost_flat[b3])
    return Stats(attack=A, strength=S, defence=D, magic=M, ranged=Ra,
                 ranged_str=Rs, hitpoints=stats.hitpoints, prayer=stats.prayer,
                 magic_str=Ms)

def apply_style_boosts(stats, style):
    """
    Given attack style and stats, apply the necessary invisible boosts.
    Valid styles are:
        "(stab|slash|crush|ranged|magic) 
         (controlled|accurate|aggressive|defensive|long|autocast)"
    """
    # Get attack type (stab, slash, crush, ranged, magic, etc.) and style
    # (accurate, aggressive, controlled, rapid, long, etc.)
    t = style.split(" ")[0]
    s = style.split(" ")[1]
    
    A, S, D, Ra, Rs, M = (stats.attack + 8,     stats.strength + 8,
                          stats.defence + 8,    stats.ranged + 8,
                          stats.ranged_str + 8, stats.magic + 8)
    old_ms = stats.magic_str
    # There's gotta be a better way to do this, but I'm too dumb to see it.
    if (t == "stab") or (t == "slash") or (t == "crush"):
        if s == "controlled":
            A, S, D = A + 1, S + 1, D + 1
        elif s == "accurate":
            A = A + 3
        elif s == "aggressive":
            S = S + 3
        elif s == "defensive":
            D = D + 3
    elif t == "ranged":
        if s == "accurate":
            Ra, Rs = Ra + 3, Rs + 3
        elif s == "long":
            D = D + 3
    elif t == "magic":
        if s == "accurate":
            M = M + 3
        elif s == "long":
            M, D = M + 1, D + 3

    return Stats(attack=A, strength=S, defence=D, magic=M, ranged=Ra,
                 ranged_str=Rs, hitpoints=stats.hitpoints, prayer=stats.prayer,
                 magic_str=old_ms)
