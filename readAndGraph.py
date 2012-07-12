import urllib2
from bs4 import BeautifulSoup

class Pot():
   
   def __init__(self,url,words,filters=lambda x: x):
      self.threadWords = words
      self.filters = filters
      self.url = url
      self.soup = self.makeSoup(self)
      
   def makeSoup(self):
      botHeaders = {'User-Agent' : '628318'} # Tau FTW
      req = urllib2.Request(self.url, headers=botHeaders)
      pageHandle = urllib2.urlopen( req )
      self.soup = BeautifulSoup(pageHandle.read())
      
   def _getLinks(self):
      links = [a_tag.get('href') for a_tag in self.soup.find_all('a') if a_tag]
      for test in self.filters:
         links = filter(test,links)
      return links
      
   def links(self):
      return self._getLinks(self)
      

class BreadthFirstSearch():
   
   def __init__(self,startingNode):
      self.depth = 0
      self.stack = [startingNode]
      self.nextLayer = []
      self.visited = {}
      
   def __len__(self):
      return len(self.stack)
      
   def __iter__(self):
      return self.next()
      
   def next(self):
      while self.stack:
         yield self.stack.pop(0)
      if self.nextLayer:
         
      
      yield None  # This signifies the end of list
      
   def append(self,nodeToAdd):
      if nodeToAdd not in self.visited:
         self.stack.append(thingToAdd)
      else:
         pass
   
   def next(self):
      nextNode = self.stack.pop(0)
      if nextNode not in self.cache:
         
      return
      
   def isEmpty(self):
      return len(self.stack) == 0
      
   def search(self,nodeList=self.stack,testMethod=lambda x: x):
      for node in nodeList:
         node = testMethod(node)
         if node:
            if node not in self.cache:
      
      
class Gephi():

   def __init__(self,inputDict):
      self.data = inputDict
      
   def asCSV(self):
      return 0 #placeholder


if __name__=='__main__':

   # Define 
   baseURL = 'http://en.wikipedia.org'
   startingURL = '/wiki/Outline_of_calculus'
   threadWords = ['Math','Mathematics','math','mathematics']
   filters = [lambda x: x, # eliminates None types - must always be first filter
              lambda x: x.startswith('/wiki'), # only keep other wikipedia links
              lambda x: x.count(':') == 0, # exclude templates
              lambda x: x.count('#') == 0] # exclude links to named sections

   myPot = Pot(startingURL,threadWords,filters)
   spider = BreadthFirstSearch(startingURL)
   depth = 0
   
   #soup.body.h2.find_all_previous(text=threadWords)
   
   while len(spider) and depth < 3;
      url = next(spider)


   