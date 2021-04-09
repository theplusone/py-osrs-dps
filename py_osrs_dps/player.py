import pandas as pd

from .helpers.player import apply_stat_boosts, apply_style_boosts
from .stats import Stats
from .gear import Gear
from .prayers import Prayers
from .boosts import Boosts

def t2s(t):
    """
    Tuple-to-stats. This is a stupid hack, but IMO, beats messing with sys.path
    to import ../stats.py from helpers/player.py.
    """
    return Stats(attack=t[0], strength=t[1], defence=t[2], magic=t[3],
                 ranged=t[4], ranged_str=t[5], hitpoints=t[6], prayer=t[7],
                 magic_str=t[8])

class Player:
    def __init__(self, stats=Stats(), gear=Gear(), prayers=Prayers(),
                 boosts=Boosts()):
        self.stats   = t2s(apply_stat_boosts(stats, prayers, boosts))
        self.stats   = t2s(apply_style_boosts(self.stats, gear.style))
        self.gear    = gear
        self.prayers = prayers
        self.boosts  = boosts
