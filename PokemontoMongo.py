# coding: utf-8

# This is an attempt at using Python to create a source file for MongoDB.

# The csv file used in this example was downloaded from https://github.com/datasets/airport-codes.  The program does the following:
#
#         It loads the csv file into the dataframe df.
#         It extracts the Country, City, Timezone and DST attributes from the full dataset into a dataframe called City; these attributes will
#		  repeat and are the same fo each city in the set, so it drops duplicates and then sorths them in ascending order by Country, City, Timezone
#		  and DST.
#         Then it defines a function writeafile that first writes 'use aviation' to the json file.  This tells the file which database to use.
#         It then iterates through a set of City rows, converts them to json format and embeds an array of airports for the city into the json record.
#         It renames the array from the standard '0' to 'Airports'.  It embeds the json into a mongoDB insert statement and writes it to the file.
#
#         The program splits the dataset into 1,000 row chunks, and writes each chunk to a file.  This is to prevent memory errors.
#
import pandas as pd
df = pd.read_csv('pokemon.csv', sep = ',',
                 delimiter = None,encoding='latin-1')
pokemon = df[['Generation', 'Type 1']]\
.drop_duplicates()\
.sort_values(['Generation','Type 1'], ascending = [True,True])

def writeafile(filename):
    file = open(filename,'w')
    print('Opening ', filename)
    rec = 'use aviation\n'
    file.write(rec)
    for r, s,  in thisfile[['Generation','Type 1']].itertuples(index=False):
        tc = (df[(df['Generation']==r) & (df['Type 1']==s)])
        j = (tc.groupby(['Generation','Type 1'], as_index=False)
        .apply(lambda x: x[['Name','Type 2','Total','HP','Attack','Defense','Sp.Attack','Sp.Def','Speed','Legendary']]
               .to_dict('r'))
             .reset_index()
             .rename(columns={0:'Pokedex'})
             .to_json(orient='records'))
        rec = 'db.Pokemon.insert(' + j + ')\n'
        file.write(rec)
    file.close()
    print('Closing ', filename)
    return()

count = 1
countmax = round(len(pokemon)+.5)/1000
print(countmax)
while (count <= countmax):
    filename = 'data/pokemon' + str(count) + '.js'
    print(filename,'start:',count*1000-1,' end: ', count*1000 + 999)
    thisfile = pokemon[count*1000 -1: count*1000 + 999]
    print(thisfile.head())
    print ('The count is:', count)
    b = writeafile(filename)
    count = count + 1

print ("Finished - GoodBye!")

