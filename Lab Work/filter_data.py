import pandas as pd
cp = pd.read_excel(r"/Users/taleb.ahsan/Documents/Folders/Work/Giachelli/T2DM WT vs T2DM KO DE.xlsx")
df = pd.DataFrame(columns=['Symbol', "Name", 'T2DM WT', 'T2DM KO', 'T2DM WT vs T2DM KO'])

counter = 0
while counter < len(cp.index):
    for index, row in cp.iterrows():
        counter += 1
        try:
            if cp.at[counter, "Compared"] > 0 and cp.at[counter, "Compared"] < 0.5:
                df = df.append({'Symbol': cp.loc[counter].at["Symbol"], 'Name': cp.loc[counter].at["Name"], 'T2DM WT': cp.loc[counter].at["T2DM WT / 174888"], 'T2DM KO': cp.loc[counter].at["T2DM KO / 174889"], 'T2DM WT vs T2DM KO':cp.loc[counter].at["Compared"]}, ignore_index=True)
            elif cp.at[counter, "Compared"] > 2:
                df = df.append({'Symbol': cp.loc[counter].at["Symbol"], 'Name': cp.loc[counter].at["Name"], 'T2DM WT': cp.loc[counter].at["T2DM WT / 174888"], 'T2DM KO': cp.loc[counter].at["T2DM KO / 174889"], 'T2DM WT vs T2DM KO':cp.loc[counter].at["Compared"]}, ignore_index=True)
        except KeyError:
            print('Done.')

print(df)
df.to_excel("/Users/taleb.ahsan/Documents/Folders/Work/Giachelli/T2DM WT vs T2DM KO.xlsx", sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None, storage_options=None)
