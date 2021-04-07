"""
Script to clean up the gear csvs a bit after pulling them from the wiki -- 
getting rid of entries that don't provide any bonuses, are duplicates, etc.

TODO: Do this in the original parse_tables.py script rather than having two
      separate scripts.
"""

import pandas as pd

df_list = []
slot_list = ["1h", "2h", "ammo", "body", "cape", "feet", "hands", "head",
             "legs", "neck", "ring", "shield"]
for slot in slot_list:
    df_list.append(pd.read_csv(f"../items/{slot}.csv"))

for i in range(len(df_list)):
    df = df_list[i]
    tmp_df = pd.DataFrame(columns=df.columns)
    for ii, row in df.iterrows():
        # Dropping prayer, atk speed, item name
        stats_i_care_about = row[1:-2]
        if list(stats_i_care_about) != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            tmp_df = tmp_df.append(row, ignore_index=True)
    # Now that I've dropped rows that have no bonuses, get rid of "#..." in
    # item names
    for ii, row in tmp_df.iterrows():
        if "#" in row["Name"]:
            item_name = tmp_df.iat[ii, 0]
            tmp_df.iat[ii, 0] = item_name[:item_name.find("#")]
    # Now that I've dropped "#..." from item names, remove duplicate rows
    tmp_df = tmp_df.drop_duplicates(ignore_index=True)
    # Write new csv
    tmp_df.to_csv(f"../items/{slot_list[i]}.csv", index=False)
