# every object has 
# type 
# internal data rep
# set of procedures to interect with object (methods)
# object is a instance of a type

type([1,2,3,4]) #<class 'list'>
type({'a':1}) #<class 'dict'>
type(1) #<class 'int'>


# methods

ratings = [1,2,.3,5,1]
ratings.sort()
ratings.reverse()

# own class
# - data attributes
# - methods

# Circle: radius color
# class: Class definition
# Circle: Name of Class
# object: Class parent
class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius += r

red_circle = Circle(10, 'red')
red_circle.radius
red_circle.radius = 15 # this would normally be done by setter
red_circle.radius

red_circle.add_radius(3) # => radius = 18

# Rectangle: height, width, color
class rectangle(object):
    def __init(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color


dir(Circle) # list all methods and attributes



class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1

# all 3 are equal

Car(make="Honda",model="Accord",color="blue")
Car("Honda","Accord","blue")
Car(model="Accord",make="Honda",color="blue")

class analysedText(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
    

class analysedText(object):
    
    def __init__ (self, text):
        self.fmtText = text.lower().replace('.','').replace('!','').replace(',','').replace('?','')
    
    def freqAll(self):      
        list_words = self.fmtText.split(' ')
        res = {}
        for word in list_words:
            val = res.get(word, 0)
            res[word] = val +1
        return res
    
    def freqOf(self,word):
        f = self.freqAll()
        return f.get(word, 0)