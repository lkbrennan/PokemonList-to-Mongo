This is an attempt at using Python to create a source file for MongoDB.

The csv file used in this example was downloaded from https://www.kaggle.com/rounakbanik/pokemon.  The program does the following:
It loads the csv file into the dataframe df.
It extracts the Generation of the Pokemon and the Type 1 attributes from the full dataset into a dataframe called Pokemon; these attributes will
repeat and are the same for each pokemon in the set, so it drops duplicates and then sorths them in ascending order by generation.
Then it defines a function writeafile that first writes 'use pokemon' to the json file.  This tells the file which database to use.
It then iterates through a set of Pokemon rows containing information about the pokemon (Name,Type 2,Total,HP,Attack,Defense,Special Attack,Special Def,Speed,Legendary Status), 
converts them to json format and embeds an array of airports for the city into the json record.
It renames the array from the standard '0' to 'Pokendex'.  It embeds the json into a mongoDB insert statement and writes it to the file.

The program splits the dataset into 1,000 row chunks, and writes each chunk to a file.  This is to prevent memory errors.