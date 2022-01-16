# This code was created to test whether I can change the parameters in order to get a smaller data file to run through IPA

import pandas as pd
cp = pd.read_excel(r"/Users/taleb.ahsan/Documents/Folders/Work/Giachelli/NC WT vs T2DM WT DE.xlsx")

counter = 0
incounter = 0
decounter = 0
while counter < len(cp.index):
    for index, row in cp.iterrows():
        counter += 1
        try:
            if cp.at[counter, 'Compared'] > 0 and cp.at[counter, 'Compared'] < 0.5:
                incounter += 1
            elif cp.at[counter, 'Compared'] > 2:
                decounter += 1
        except KeyError:
            print("done")
print(incounter, decounter)
