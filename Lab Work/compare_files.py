import pandas as pd
cp = pd.read_excel(r"/Users/taleb.ahsan/Documents/Folders/Work/Giachelli/T2DM WT vs T2DM KO Pathways.xls")
cp2 = pd.read_excel(r"/Users/taleb.ahsan/Documents/Folders/Work/Giachelli/Aikawa CAVD Diseased Fibrosa Leaflet Layer Pathways.xlsx")

def regulation_score(full_str):
	frac, horse = full_str.split(" ")
	num, denom = frac.split("/")
	value = float(num) / float(denom)
	return value

counter = 0
full_list = []
list_of_pathways_1 = []
pathway_and_regulation_score = []
distinct_pathways_1 = []
regulation_status = []
distinct_pathways_2 = []


for item in cp["Ingenuity Canonical Pathways"]:
	pathway_and_regulation_score = []
	pathway_and_regulation_score.append(item)
	if regulation_score(cp.loc[counter].at["Downregulated"]) > regulation_score(cp.loc[counter].at["Upregulated"]):
		pathway_and_regulation_score.append("Downregulated")
	elif regulation_score(cp.loc[counter].at["Downregulated"]) < regulation_score(cp.loc[counter].at["Upregulated"]):
		pathway_and_regulation_score.append("Upregulated")
	else:
		pathway_and_regulation_score.append("Neither")
	list_of_pathways_1.append(pathway_and_regulation_score)
	counter += 1

counter = 0
for pathway in list_of_pathways_1:
	word_list_1 = pathway[0].split(" ")
	
	for item in cp2["Pathway"]:
		word_list_2 = item.split(" ")

		banned_words = ['Signaling', 'signaling', 'Pathway', 'pathway', 'Of', 'of', 'by', 'By', 'From', 'from', 'The', 'the', 'And', 'and', 'In', 'in', 'Regulation', 'regulation', 'Inhibition', 'inhibition', 'Formation', 'formation', 'Role', 'role', 'System', 'system', 'Cell', 'cell', 'Activation', 'activation', 'Receptor', 'receptor', 'Receptors', 'receptors' '/']
		for word in banned_words:
			if word in word_list_1:
				word_list_1.remove(word)
			if word in word_list_2:
				word_list_2.remove(word)

		for word in word_list_1:
			for word2 in word_list_2:
				if word == word2:
					if pathway[0] not in full_list:
						distinct_pathways_1.append(pathway[0])
						regulation_status.append(pathway[1])
						full_list.append(pathway[0])
					if item not in full_list:
						distinct_pathways_2.append(item)
						full_list.append(item)


df = pd.DataFrame()

df["T2DM WT vs T2DM KO Pathways"] = distinct_pathways_1
df["Upregulated or Downregulated"] = regulation_status
dp2 = pd.Series(distinct_pathways_2)
df["Aikawa CAVD Diseased Fibrosa Leaflet Layer Pathways"] = dp2


df.to_excel(r"/Users/taleb.ahsan/Desktop/T2DM WT vs T2DM KO vs Aikawa CAVD Diseased Fibrosa Leaflet Layer Pathways.xlsx")
