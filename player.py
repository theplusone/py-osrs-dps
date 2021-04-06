import pandas as pd
import playerhelpers as ph
from stats import Stats
from gear import Gear
from prayers import Prayers
from boosts import Boosts

class Player:
    def __init__(self, stats=Stats(), gear=Gear(), prayers=Prayers(),
                 boosts=Boosts()):
        print(f"Magic before apply_stats_boosts: {stats.magic}")
        self.stats   = ph.apply_stat_boosts(stats, prayers, boosts)
        print(f"Magic after apply_stats_boosts: {self.stats.magic}")
        self.stats   = ph.apply_style_boosts(self.stats, gear.style)
        print(f"Magic after apply_style_boosts: {self.stats.magic}")
        self.gear    = gear
        self.prayers = prayers
        self.boosts  = boosts
