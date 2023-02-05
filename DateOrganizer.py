# Add your code here
#Create a class Date that has three attributes (day, month, and year) initialized through the constructor.

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return 'day:{},month:{},year:{}'.format(self.day,self.month,self.year) 

#Create a class DateTime that inherits from Date date and adds the attributes 
# representing the hours minutes and seconds that are also initialized in through the constructor of the DateTime class.
class DateTime(Date):
    def __init__(self, day, month, year, hour, minute, second):
        super().__init__(day, month, year)
        self.hour = hour
        self.minute = minute
        self.second = second
#Override the definition of str with an implementation that utilizes the definition in the parent and concatenates the time components to it with the format ‘day:<day-value>,month:<month-value>,year:<year-value>--<hrs>:<mins>:<secs>
#E.g. 'day:1,month:3,year:2020--11:22:33'
    def __str__(self):
        return super().__str__() + '--{}:{}:{}'.format(self.hour, self.minute, self.second)

#Define a stand-alone function that receives one argument representing one of the known date 
#formats and returns a function object that remembers the specified format.
#format can be one of the following: bigEndian, littleEndian, middleEndian
#dateParser(format) -> function object that remembers the format
def dateParser(format):
    #*args is a tuple of arguments - allows us to pass a variable number of non-keyword arguments to a function
    def parse(*args):
        parsedDates = []
        for date in args:
            if format == 'bigEndian':
                #comma forms a tuple, which in Python looks just like an immutable list.
                year, month, day = date.split('-')
                #.append() adds an item to the end of the list
                #Date is the class above and day, month, year are the arguments
                parsedDates.append(Date(day, month, year))
            elif format == 'littleEndian':
                day, month, year = date.split('-')
                parsedDates.append(Date(day, month, year))
            elif format == 'middleEndian':
                month, day, year = date.split('-')
                parsedDates.append(Date(day, month, year))
        return parsedDates
        #parse is the function that is returned
    return parse


#The actual parser function that would be returned can receive an arbitrary number of 
# strings of dates to parse them according to the format that was specified beforehand and return a list of Date objects representing the given dates.





# The following code is used to test your implementation






# Please use the following names to recieve the corresponding functions as they return from the outer function calls
bigEndianParser = dateParser('bigEndian')
littleEndianParser = dateParser('littleEndian')
middleEndianParser = dateParser('middleEndian')






# Testing
#test_DateObjectCreation() - tests the creation of a Date object
def test_DateObjectCreation():
    d = Date('1','3','2020')
    assert d.__str__() == 'day:1,month:3,year:2020'

def test_DateTimeObjectCreation():
    dt = DateTime('1','3','2020', '11','22','33')
    assert dt.__str__() == 'day:1,month:3,year:2020--11:22:33'


def testBigEndian1():
    parsedDates = bigEndianParser('2021-03-31')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    
    
def testBigEndian3():
    parsedDates = bigEndianParser('2021-03-31','2020-04-5','2019-05-15')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    assert parsedDates[1].__str__() == 'day:5,month:04,year:2020'
    assert parsedDates[2].__str__() == 'day:15,month:05,year:2019'

def testLittelEndian1():
    parsedDates = littleEndianParser('31-03-2021')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    
    
def testLittelEndian3():
    parsedDates = littleEndianParser('31-03-2021','5-04-2020','15-05-2019')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    assert parsedDates[1].__str__() == 'day:5,month:04,year:2020'
    assert parsedDates[2].__str__() == 'day:15,month:05,year:2019'

def testMiddleEndian1():
    parsedDates = middleEndianParser('03-31-2021')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    
    
def testMiddleEndian3():
    parsedDates = middleEndianParser('03-31-2021','04-5-2020','05-15-2019')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    assert parsedDates[1].__str__() == 'day:5,month:04,year:2020'
    assert parsedDates[2].__str__() == 'day:15,month:05,year:2019'
