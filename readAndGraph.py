import urllib2
from bs4 import BeautifulSoup

class BreadthFirstSearch():
   
   def __init__(self,depthLimit):
      self.stack = []
      self.cache = {}
      self.maxDepth = depthLimit
      
   def append(self,thingToAdd):
      if not self.hasBeenSearched(thingToAdd):
         self.stack.append(thingToAdd)
   
   def next(self):
      return self.stack.pop(0)
      
   def isEmpty(self):
      return len(self.stack) == 0
      
   def currentDepth(self):
      return self.stack[0]
      
   def hasBeenSearched(self,node):
      return node in self.cache
      
if __name__=='__main__':
   startingURL = 'http:' + '//en.wikipedia.org/wiki/Outline_of_calculus'
   threadWords = ['Math','Mathematics','math','mathematics']
   
   spiderMan = BreadthFirstSearch(3)
   
   linkStack.append(startingURL)
depth = 0

"""
req = urllib2.Request(startingURL, headers={'User-Agent' : '6283185307'}) # Tau FTW
pageHandle = urllib2.urlopen( req )
soup = BeautifulSoup(pageHandle.read())

print soup.body.find(text='Contents').find_all_previous(text=threadWords,limit=1)

"""

while len(linkStack) and depth < 3:
   parentURL = linkStack.pop(0)
   if parentURL not in vistedStack:
      visitedStack[parentURL] = {}
   req = urllib2.Request(parentURL, headers={'User-Agent' : '628318'}) # Tau FTW
   pageHandle = urllib2.urlopen( req )
   soup = BeautifulSoup(pageHandle.read())
   
   
   

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
   