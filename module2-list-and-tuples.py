ratings = (10, 9 , 6, 5, 10, 8, 9, 6, 2) # <class 'tuple'>

tuple1 = ('disco', 10, 1.2) # different types inside the tuple

tuple1[0] # => 'disco'
tuple1[1] # => 10
tuple1[2] # => 1.2

tuple1[-3] # => 'disco'

tuple2 = tuple1 + ('hardrock', 10) #=> ('disco', 10, 1.2,hardrock', 10)
tuple2[:3] # => slice the tuple first 2 element


# tuples are immutable
tuple2[4] = '1234' # error


# need to create new tuple if want a different one
ratings_sorted = sorted(ratings)
type(ratings_sorted) # list

# tuple nesting 
nt = (1,2,('pop', 'rock'), (3,4),('disco', (1,2)))

nt[2] # => ('pop','rock)
nt[2][1] # => 'rock'
nt[4][1][0] #=> 1

# list are mutable
l = ['Michael Jackson', 10.1, 1982, [1,2], ('A', 1)]

l[1] # => 10.1

l[-1] # => (A,1)

l[3:] #[[1, 2], ('A', 1)]
l[3:5] # => [[1, 2], ('A', 1)]

# concat returns a new list
l + ['pop', 10] # => ['Michael Jackson', 10.1, 1982, [1,2], ('A', 1), 'pop', 10]

# l.extend modifies inplace the list
l2 = [1,2,3,4]
l2.extend([5,6]) # [1,2,3,4,5,6]
l2.append([7,8]) # [1,2,3,4,5,6,[7,8]]
# modify
l[0] = 'Hard rock'
# deliete an element
del(l[2])

"hard rock".split() # => ['hard', 'rock']
'a,b,c,d'.split(',') # => ['a', 'b', 'c', 'd']

list_a = ['a','b','c']
list_b = list_a
# list_b references the same list as list_a
list_b[0] = 'banana'
list_a[0] # => 'banana

# copy of list a
list_a = ['a','b','c']
list_b = list_a[:]
list_b[0] = 'banana'
list_a[0] # => 'a'

help(list_a)


genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 

genres_tuple.index('disco') # => 7
'disco' in genres_tuple # => True