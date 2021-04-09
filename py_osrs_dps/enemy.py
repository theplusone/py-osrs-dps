from .helpers.raids import scale_stats

class Enemy:
    def __init__(self, stats, scale=1):
        self.stats = scale_stats(stats, scale)
        self.scale = scale
