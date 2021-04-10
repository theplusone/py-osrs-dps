from .helpers.raids import scale_stats
from .helpers.enemy import drain_defence

class Enemy:
    def __init__(self, stats, scale=1, size=3, dwh=0, bgs=0, arclight=0):
        self.stats = scale_stats(stats, scale)
        self.stats = drain_defence(self.stats, dwh, bgs, arclight)
        self.scale = scale
        self.size  = size