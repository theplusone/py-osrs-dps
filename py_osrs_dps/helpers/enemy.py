import math

def drain_defence(stats, dwh, bgs, arclight):
    stats = stats.copy(deep=True)
    defence = stats["Defence level"]

    # Apply Arclight drains
    defence = math.ceil(defence - defence * 0.05 * arclight)

    # Apply DWH drains
    for _ in range(0, dwh):
        defence = defence * 0.7
    defence = math.ceil(defence)

    # Apply BGS drains
    defence = defence - bgs

    # Can't go below 0
    if defence < 0:
        defence = 0

    # Can't go below defence floor either
    if defence < stats["Def floor"]:
        defence = stats["Def floor"]

    stats["Defence level"] = defence
    return stats
