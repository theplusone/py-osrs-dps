# py-osrs-dps

`!!! MAX BIG FAN !!!`

## Current status

**Semi-working**

This code (seemingly) provides accurate DPS calcs _if and only if_:
- Your gear setup does not have any set bonuses (e.g. void, inquisitors)
- You're not taking advantage of enemy attributes (e.g. arclight on demons,
  lance on dragons, salve on undead, tbow on CoX monsters,
  [etc.](https://oldschool.runescape.wiki/w/Monster_attribute))
- You're soloing raids (all NPCs assume 1-man stats right now)
- You're not fighting something where the attack and defence rolls vary from the
  norm
  - e.g. Ice Demon, who uses regular defence instead of mage defence for defence
    rolls

## What is this?

py-osrs-dps is (supposed to be) an OldSchool RuneScape DPS calculator for
Python.

The eventual goal is to have an easy and programmatic way to run bulk DPS calcs.
This would be helpful for e.g. the upcoming blowpipe nerf -- using this could
save a lot of time over manually adjusting values and setting gear in the DPS
spreadsheet (the DPS spreadsheet is an amazing tool, though).

From there, it'd be neat to take the output from this tool and use it to
generate something presentable (fancy image, website, etc.).

## What's done so far?

- List of gear/items
  - `parse_table.py` in util/ can parse slot tables from the wiki;
    `parse_all_tables.sh` runs the script for all slot tables.
- List of NPCs
  - Taken from the DPS spreadsheet. Scaling formulas for raids NPCs were found,
    but how I'll implement them remains to be seen.
- test.py
  - Mostly scratchwork/goofing off/testing stuff goes in here before I move
    stuff around to a more permanent location. Try running it
    (`python3 -i test.py`) and playing around.

## Stuff to do

- ~~Figure out how DPS calcs work~~
  - ~~The formulas are well-known, but not to me. lol~~ I've got a decent grasp
    on the formulas now
- ~~Import a list of gear/items~~
  - ~~With some effort and cleanup, I might be able to rip this from the
    spreadsheet~~
- ~~Import a list of NPCs~~
  - Determine some way to account for exceptions to normal NPC stats, e.g. ...
    - ~~How are raids bosses scaled?~~ Formulas can be found in DPS spreadsheet
      under "NPC stats" sheet
    - How can I program Ice Demon to use regular defence rather than mage level
      for magic defense rolls?
- Handle all/most of the gear/set bonuses
- General code cleanup
- TBD
  - I'm not good at planning things. I'll add more issues to this list as they
    come up.
