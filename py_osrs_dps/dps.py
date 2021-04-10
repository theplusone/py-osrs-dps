from .helpers.dps import (calc_max_hit, calc_atk_roll, calc_def_roll,
                          calc_accuracy, calc_dps)

class DPS:
    def __init__(self, you, enemy):
        self.you = you
        self.enemy = enemy
        # Stuff needed for DPS
        self.max_hit  = calc_max_hit(you.stats, you.gear, enemy.size)
        self.atk_roll = calc_atk_roll(you.stats, you.gear)
        self.def_roll = calc_def_roll(you.gear.style.split(" ")[0], enemy.stats)
        self.accuracy = calc_accuracy(self.atk_roll, self.def_roll)
        # Damage-per-hit
        self.dph      = (self.max_hit * self.accuracy) / 2
        # Damage-per-second!
        self.dps      = calc_dps(self.dph, you.gear)