#METHOD 1
def solve(s):
    return ' '.join(i.capitalize()   for i in s.split(' '))

#METHOD 2
import string
def solve(s):    
     return string.capwords(s,' ')