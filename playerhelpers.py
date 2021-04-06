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
    A, S, D, Ra, Rs, M = (stats.attack, stats.strength, stats.defence,
                          stats.ranged, stats.ranged_str, stats.magic)
    p1, p2, p3 = (prayer.melee, prayer.ranged, prayer.magic)
    b1, b2, b3 = (boost.melee, boost.ranged, boost.magic)
    attack    = int((int(A * boost_coeff[b1]) + boost_flat[b1])
                    * prayer_coeff["Attack"][p1])
    strength  = int((int(S * boost_coeff[b1]) + boost_flat[b1])
                    * prayer_coeff["Strength"][p1])
    defence   = int((int(D * boost_coeff[b1]) + boost_flat[b1])
                    * prayer_coeff["Defence"][p1])
    ranged_a  = int((int(Ra * boost_coeff[b2]) + boost_flat[b2])
                    * prayer_coeff["Ranged (a)"][p2])
    ranged_s  = int((int(Rs * boost_coeff[b2]) + boost_flat[b2])
                    * prayer_coeff["Ranged (s)"][p2])
    magic     = int((int(A * boost_coeff[b3]) + boost_flat[b3])
                    * prayer_coeff["Magic"][p3])
    return Stats(attack=attack, strength=strength, defence=defence,
                 magic=magic, ranged=ranged_a, hitpoints=stats.hitpoints,
                 prayer=stats.prayer, ranged_str=ranged_s)
