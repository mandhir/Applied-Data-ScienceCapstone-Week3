import pandas as pd
from pandas.io.html import read_html

url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

table = pd.read_html(url)

df = table[0]

pcode = df

header = pcode.iloc[0]

pcode.rename(columns = header, inplace = True)

pcode.drop([0,0], axis = 0, inplace = True)

pcode = pcode[pcode['Borough'] != 'Not assigned']

pcode.reset_index(drop = True, inplace = True)


for index, row in pcode.iterrows():
     if (row[2] == "Not assigned"):
        pcode.at[index, 'Neighbourhood'] = row[1]

postalcodes = pcode['Postcode'].unique()

pcodes_collapsed = pd.DataFrame([])

for i, code in enumerate(postalcodes):
        temp = pcode[pcode['Postcode'] == code]
        separator = ', '
        hoods = separator.join(list(temp['Neighbourhood']))
        temp.at[(temp.index)[0], 'Neighbourhood'] = hoods
        pcodes_collapsed = pcodes_collapsed.append(temp.iloc[0], ignore_index = True)

pcodes_collapsed = pcodes_collapsed[['Postcode', 'Borough', 'Neighbourhood']]

print(pcodes_collapsed.shape)

