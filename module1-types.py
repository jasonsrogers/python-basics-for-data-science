type(11) # <class 'int'>
type(21.213) # <class 'float'>
type('A string') # <class 'str'>


# Type casting 

float(2) # => 2.0
int(1.1) # => 1
int(1) # => 1
int('1') # => 1
int('a') # => error: ValueError: invalid literal for int() with base 10:

str(1)
str(1.1)

# Booleans
True
False

type(True) # => <class 'bool'>

int(True) # => 1
int(False) # => 0

bool(1) # => True
bool(1000) # => True
bool(0) # => False
