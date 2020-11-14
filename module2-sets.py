# sets are a type of collection 
# unordered 
# uniq elements

set1 = {'pop', 'rock', 'soul', 'hard rock', 'rock', 'R&B', 'disco'}
# set1 = {'R&B', 'rock', 'pop', 'soul', 'disco', 'hard rock'}

# cast list to set 
set2 = set(['pop', 'rock', 'soul', 'hard rock', 'rock', 'R&B', 'disco'])

# operations
set3 = { 'thriller', 'back in black', 'AC/DC'}
set3.add('NSYNC')
set3.add('NSYNC')
set3.add('NSYNC')
set3.add('NSYNC')
#{'AC/DC', 'NSYNC', 'thriller', 'back in black'}

set3.remove('NSYNC')

#{'AC/DC', 'thriller', 'back in black'}

'AC/DC' in set3 # True
'Back' in set3 # False

album_set_1 = {'AC/DC', 'Back in Black', 'Thriller'}
album_set_2 = {'AC/DC', 'Back in Black', 'The Dark Side of the Moon'}

album_set_1 & album_set_2 # => intersection {'Back in Black', 'AC/DC'}
album_set_1.intersection(album_set_2) #=> {'Back in Black', 'AC/DC'}
# NOT the same as logical operator "and"
album_set_1 and album_set_2 # => this returns album_set_1


album_set_1.union(album_set_2) # => {'Thriller', 'The Dark Side of the Moon', 'Back in Black', 'AC/DC'}

# diff of what is in 1 but not in 2
album_set_1.difference(album_set_2) # => 'Thriller'
# diff of what is in 1 but not in 2
album_set_2.difference(album_set_1) # => 'The Dark Side of the Moon'




album_set_3 = {'AC/DC', 'Back in Black'}

album_set_3.issubset(album_set_1) # => True

set({"Back in Black", "AC/DC"}).issubset(album_set_1)  #=> True
album_set_1.issuperset({"Back in Black", "AC/DC"})   # => True