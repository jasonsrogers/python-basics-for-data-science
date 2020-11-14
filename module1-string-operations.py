"Michael Jackson"
"12345"
"!(*$%!)@(*%)(!*"

name = "Michael Jackson"
name[0] # => M
name[13] # => o
name[-3] # => s

name[0:4]# => Mich
name[8:12]# => Jack

name[::2]# => every second variable McelJcsn
name[0:5:2]# => every second variable from 0 to 5 excluded => Mce

len("Michael Jackson")
len(name) # => 15

statement = name + " is the best" # => Michael Jackson is the best

name * 3 # 'Michael JacksonMichael JacksonMichael Jackson'

print('Michael Jackson \n is the best!')
print('Michael Jackson \t is the best!')# => Michael Jackson          is the best!
print('Michael Jackson \\t is the best!')# => Michael Jackson \t is the best!
print(r'test \t something')# => test \t something

# String Methods
A = "Thriller is the sixth studio album"
B = A.upper() # => B = 'THRILLER IS THE SIXTH STUDIO ALBUM' 
# A is still "Thriller is the sixth studio album"

A = 'Michael Jackson is the best'
B = A.replace('Michael','Janet')# B =>'Janet Jackson is the best'
# A => 'Michael Jackson is the best'

name.find('el') #5
name.find('Jack') #8
name.find('a') #4




