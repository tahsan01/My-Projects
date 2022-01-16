#!/usr/bin/env python3
# Here, I am importing pandas and creating the reader (cp) via pandas. df is the new dataframe in which
# I will store the relevant data extracted from the original spreadsheet.

import pandas as pd
cp = pd.read_excel(r"/Users/taleb.ahsan/Documents/Folders/Work/Giachelli/NC WT vs T2DM WT DE.xlsx")
df = pd.DataFrame(columns=['Symbol', "Name", 'NC WT', 'T2DM WT'])
# df = df.append({"Symbol":6000, "Name":40, "NC WT":40, "T2DM":40}, ignore_index = True, verify_integrity = False, sort = False)

counter = 0
# relevant_dictionary = {}
while counter < len(cp.index):
    for index, row in cp.iterrows():
        counter += 1
        try:
            if cp.at[counter, 'Compared'] > 0 and cp.at[counter, 'Compared'] < 0.75:
                # relevant_dictionary[cp.loc[counter].at["Symbol"]] = cp.at[counter, 'Compared']
                # print(cp.at[counter, 'Compared'])
                df = df.append({'Symbol': cp.loc[counter].at["Symbol"], 'Name': cp.loc[counter].at["Name"], 'NC WT': cp.loc[counter].at["NC WT / 174886"], 'T2DM WT': cp.loc[counter].at["T2DM WT / 174888"]}, ignore_index=True)

            elif cp.at[counter, 'Compared'] > 1.75:
                # relevant_dictionary[cp.loc[counter].at["Symbol"]] = cp.at[counter, 'Compared']
                # print(cp.at[counter, 'Compared'])
                df = df.append({'Symbol': cp.loc[counter].at["Symbol"], 'Name': cp.loc[counter].at["Name"], 'NC WT': cp.loc[counter].at["NC WT / 174886"], 'T2DM WT': cp.loc[counter].at["T2DM WT / 174888"]}, ignore_index=True)

        except KeyError:
            print("KeyError. That's all.")
# print(relevant_dictionary)

# print(cp.at[counter,'Compared'])
# print(cp.at[counter,'Name'])
print(df)
df.to_excel("/Users/taleb.ahsan/Documents/Folders/Work/Giachelli/NC WT vs T2DM WT.xlsx", sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None, storage_options=None)
# use cp.to_excel to write the new values to another excel spreadsheet
