import sys
import traceback
from HTMLParser import HTMLParseError
def formatExceptionInfo(maxTBlevel=5):
   cla, exc, trbk = sys.exc_info()
   excName = cla.__name__
   try:
         excArgs = exc.__dict__["args"]
   except KeyError:
         excArgs = "<no args>"
   excTb = traceback.format_tb(trbk, maxTBlevel)
   return (excName, excArgs, excTb)

from bs4 import BeautifulSoup
s = """
<html>
<script>
var pstr = "<li><font color='blue'>1</font></li>";
for(var lc=0;lc<o.length;lc++){}
</script>
</html>
"""

try:
   p = BeautifulSoup(s)

except HTMLParseError:
   print 'Ding!'
   




"""

class Thing():

   def __init__(self):
      self.alist = [1,2,3,4,5]
      self.blist = [6,7,8,9,10]
      self.layers = 0

   def __iter__(self):
      return self.next()
      
   def next(self):
      while self.alist:
         yield self.alist.pop(0)
         if not self.alist and self.blist:
            self.layers += 1
            self.alist.extend(self.blist)
            self.blist = []


A = Thing()

for thing in A:
   print thing

print 'there are {} layers'.format(A.layers)
  
"""
"""
  
################# Part 1 #######################

import urllib2
from bs4 import BeautifulSoup

baseURL = 'http://en.wikipedia.org'
#startingURL = baseURL + '/wiki/outline_of_calculus'
#startingURL = baseURL + '/wiki/calculus'
startingURL = baseURL + '/wiki/Limit_(mathematics)'
threadWords = ['Math','Mathematics','math','mathematics']

filters = [lambda x: x, # eliminates None types - must always be first filter
           lambda x: x.startswith('/wiki'), # only keep other wikipedia links
           lambda x: x.count(':') == 0,
           lambda x: x.count('#') == 0,
           lambda x: not x.endswith('(disambiguation)')]

req = urllib2.Request(startingURL, headers={'User-Agent' : '6283185307'}) # Tau FTW
pageHandle = urllib2.urlopen( req )
soup = BeautifulSoup(pageHandle.read())

#print soup.body.find(text='Contents').find_all_previous(text=threadWords,limit=1)
#print soup.prettify()
#print soup.body.find(text='Contents').find_all_previous()
#print soup.body.h2.find_all_previous(text=threadWords)

#print soup.find(id='bodyContent').find('p')
#print soup.find(id='bodyContent').p.find_all(text=threadWords)

for stuff in soup.find(id='bodyContent').find(id='toc').find_all_previous('p'):
   print stuff.find(text=threadWords)


############## End Part 1 #######################
"""

"""
#################### USELESS ##################
# Alternate way of running the tests. Define the validation function outside
# the object, and pass it in when you instantiate

#define the validation function
def validate(*args,**kargs):
   print args[0]
   if not args[0]: # eliminate None types
      print 'None type fail'
      return False
   elif not args[0].startswith('/wiki'):
      print 'not a wiki link'
      return False
   elif not args[0].count(':') == 0:
      print 'has a colon'
      return False
   elif not args[0].count('#') == 0:
      print 'has a hash'
      return False
   else:
      print 'valid link'
      return True

#define your object
class Thing1():

   def __init__(self,testFunction):
      self.test = testFunction      # pass in the validation function
      
   def getLinks(self,alist):
      return filter(self.test,alist)

aThing = Thing1(validate)

someLinks = [None,'abc','/wiki/a:b','/wiki/a#b','/wiki/abc']

# Now we can filter a list using test
print 'someLinks before filter'
print someLinks
print 'someLinks during filter'
someLinks = aThing.getLinks(someLinks)
print 'someLinks after filter'
print someLinks

#################### END USELESS ##############
"""

"""
links = [a_tag.get('href') for a_tag in soup.find_all('a') if a_tag]
for test in filters:
   links = filter(test,links)
   
for link in links:
   print link

"""

"""

while len(linkStack) and depth < 3:
   parentURL = linkStack.pop(0)
   if parentURL not in vistedStack:
      visitedStack[parentURL] = {}
   req = urllib2.Request(parentURL, headers={'User-Agent' : '628318'}) # Tau FTW
   pageHandle = urllib2.urlopen( req )
   soup = BeautifulSoup(pageHandle.read())
   
   #tests
   # lambda x: x
   # lambda x: x.startswith('/wiki')
   # lambda x: x.count('#') == 0
   # lambda x: x.count(':') == 0
   

   for link in soup.find_all('a'):
      href = link.get('href')
      if href and href.startswith('/wiki'): #Not None, and within wikipedia
         if href.count('#') == 0 and href.count(':') == 0: #Not on this page
            if href not in visitedStack:
               linkStack.append(href)
               visitedStack[href] = {}
               visitedStack[href][parentURL] = None
            else:
               if parentURL not in linkStack[href]:
                  linkStack[href][parentURL] = None
         
            
for key in linkStack:
   print '{0}\t{1}'.format(len(linkStack[key]),key)
   
"""
