# collection that as keys and values 
# keys usually characts
# creates {}

{'key1': 1, 'key2': '2', 'key3': [3,3,3], 'key4': (4,4,4), ('key5'): 5}


dict_movies = {'Thriller': 1982, 'Back in Black': 1980}

dict_movies['Thriller'] # => 1982

dict_movies['Graduation'] = 2007 # => adds an entry 'Graduation' with value 2007

del(dict_movies['Thriller']) # => removes the entry Thriller

'Back in Black' in dict_movies # => True

dict_movies.keys()
dict_movies.values()
dict_movies.items() # => list of tuples key/value
