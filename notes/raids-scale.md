# Raids scaling

Some notes on how raids scaling might work with Bitterkoekje's DPS calculator.
According to the spreadsheet itself, it's only accurate for up to 5 players.

NPC stats seem to be looked up in Sheet 1.

## TL;DR / Scaling formulas

To find the formulas yourself, look at the "NPC stats" sheet, click on the cell
of the stat you want (e.g. Great Olm (head) -> Hitpoints), and you'll see the
formula in the formula bar.

All of these are rounded _down_ to the nearest integer (e.g. 240.9 -> 240)
unless otherwise specified. _N_ is the number of players in the raid.

**Great Olm (head)**
```
      HP: 400 + (400 * N)
  Attack: N = 1 | 250
          N > 1 | 250 * (1 + (0.07 * (1 + int(N/5))) + 0.01 * (N - 1))
Strength: Same as ATK.
 Defence: 150 * (1 + (0.01 * (N - 1)))
   Magic: Same as ATK.
  Ranged: Same as ATK.
```

The melee and mage hands use the same formulas, just with different base
numbers.

- Melee hand
  - HP: Replace 400 with 300.
  - Defence: Replace 150 with 175.
  - Magic: Replace 250 with 175.
- Mage hand
  - HP: Replace 400 with 300.
  - Attack: Replace 250 with 272.
  - Strength: Replace 250 with 272.
  - Defence: Replace 150 with 175.
  - Magic: Replace 250 with 87.
  - Ranged: Replace 250 with 272.

## Attack

Raw formula
```
=ceiling(INDEX('NPC stats'!$A$2:$Z,MATCH($B$75,'NPC stats'!$A$2:$A,0),MATCH('NPC stats'!$F$2,'NPC stats'!$A$2:$2,0))*(1-E100))
```

Slightly prettified formula
```
=ceiling(INDEX('NPC stats'!A2:Z,
               MATCH(B75, "NPC stats"!A2:A, 0),
               MATCH("NPC stats"!F2, "NPC stats"!A2:2,0))
         * (1 - E100))
```

The first `MATCH()` returns the relative position of the given NPC (whose name
is in B75).

The second `MATCH()` returns the relative position of the "Attack level" column
from the array/list of stat columns (combat level, hitpoints, attack, strength,
etc...).

`'NPC stats'!A2:Z` refers to [this region](https://i.imgur.com/siUedJa.png)
highlighted in blue. It continues to the bottom of the sheet.

`INDEX()` returns the content of a cell, given:
- a reference ("NPC stats"!A2:Z)
- a row offset (the first MATCH())
- a column offset (the second MATCH())

So all this really does is look up the given attack level from the NPC stats
sheet. The last little piece `(1 - E100)` is an Arclight multiplier. E100 is
0.05 (0.10 if demon) * number of landed Arclight specs.

`ceiling()` just rounds up to the nearest integer (e.g. 24.1 -> 25).

```
=ceiling(Attack level from "NPC stats" sheet * Arclight multiplier)
```

To the right of this cell is more or less a copy of this cell that gets
subtracted by BGS attack drain.

## Strength

Strength works the same as attack, just with one slightly different offset to
hit the strength column rather than the attack column.

---

So, I wasted a bunch of time breaking that down and typing it all out, but I'm
still not sure how the raid scaling works... let's change the scale number and
see what happens, I guess...?

Okay, so changing the scale number actually affects the stats in the "NPC stats"
sheet itself. And... yeah. Looks like the formulas are right there.
