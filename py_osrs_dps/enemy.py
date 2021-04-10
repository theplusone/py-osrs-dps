from .helpers.raids import scale_stats

class Enemy:
    def __init__(self, stats, scale=1, size=3):
        self.stats = scale_stats(stats, scale)
        self.scale = scale
        self.size  = size