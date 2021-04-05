# py-osrs-dps

## Current status

**Brand new project (i.e. not working yet).**

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

## Stuff to do

- Figure out how DPS calcs work
  - The formulas are well-known, but not to me. lol
- ~~Import a list of gear/items~~
  - ~~With some effort and cleanup, I might be able to rip this from the
    spreadsheet~~
- Import a list of NPCs
  - Determine some way to account for exceptions to normal NPC stats, e.g. ...
    - How are raids bosses scaled?
    - How can I program Ice Demon to use regular defence rather than mage level
      for magic defense rolls?
- TBD
  - I'm not good at planning things. I'll add more issues to this list as they
    come up.
