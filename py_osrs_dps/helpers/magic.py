# Magic base max hits

standard_spells = {
    "Wind Strike"       : 2,
    "Water Strike"      : 4,
    "Earth Strike"      : 6,
    "Fire Strike"       : 8,
    "Wind Bolt"         : 9,
    "Water Bolt"        : 10,
    "Earth Bolt"        : 11,
    "Fire Bolt"         : 12,
    "Wind Blast"        : 13,
    "Water Blast"       : 14,
    "Crumble Undead"    : 15,
    "Earth Blast"       : 15,
    "Fire Blast"        : 16,
    "Wind Wave"         : 17,
    "Water Wave"        : 18,
    "Earth Wave"        : 19,
    "Saradomin Strike"  : 20,
    "Claws of Guthix"   : 20,
    "Flames of Zamorak" : 20,
    "Fire Wave"         : 20,
    "Wind Surge"        : 21,
    "Water Surge"       : 22,
    "Earth Surge"       : 23,
    "Fire Surge"        : 24,
    "Iban Blast"        : 25
}

ancient_spells = {
    "Smoke Rush"     : 13,
    "Shadow Rush"    : 14,
    "Blood Rush"     : 15,
    "Ice Rush"       : 16,
    "Smoke Burst"    : 17,
    "Shadow Burst"   : 18,
    "Blood Burst"    : 21,
    "Ice Burst"      : 22,
    "Smoke Blitz"    : 23,
    "Shadow Blitz"   : 24,
    "Blood Blitz"    : 25,
    "Ice Blitz"      : 26,
    "Smoke Barrage"  : 27,
    "Shadow Barrage" : 28,
    "Blood Barrage"  : 29,
    "Ice Barrage"    : 30
}

powered_spells = {
    "Seas built-in"        : 20,
    "Swamp built-in"       : 23,
    "Sanguinesti built-in" : 24
}

spells = {}
spells.update(standard_spells)
spells.update(ancient_spells)
spells.update(powered_spells)
