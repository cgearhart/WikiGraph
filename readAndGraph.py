import urllib2
from bs4 import BeautifulSoup

class Pot():
   
   def __init__(self,url,words,filters=lambda x: x):
      self.threadWords = words
      self.filters = filters
      self.soup = self.makeSoup(url)
      
   def makeSoup(self,url):
      botHeaders = {'User-Agent' : '628318'} # Tau FTW
      req = urllib2.Request(url, headers=botHeaders)
      pageHandle = urllib2.urlopen( req )
      return BeautifulSoup(pageHandle.read())
   
   def _getLinks(self):
      links = [a_tag.get('href') for a_tag in self.soup.find_all('a') if a_tag]
      for test in self.filters:
         links = filter(test,links)
      return links
      
   def links(self):
      return self._getLinks()
      

class BreadthFirstSearch():
   
   def __init__(self,startingNode):
      self.stack = [startingNode]
      self.cache = {}
      
   def __len__(self):
      return len(self.stack)
      
   def append(self,nodeToAdd):
      if nodeToAdd not in self.cache:
         self.stack.append(thingToAdd)
      else:
         pass
   
   def next(self):
      nextNode = self.stack.pop(0)
      if nextNode not in self.cache:
         pass
      return
      
   def isEmpty(self):
      return len(self.stack) == 0
      
   def search(self,nodeList=None,testMethod=lambda x: x):
      if not nodeList:
         nodeList = self.stack
      for node in nodeList:
         node = testMethod(node)
         if node:
            if node not in self.cache:
               pass
   


class Gephi():

   def __init__(self,inputDict):
      self.data = inputDict
      
   def asCSV(self):
      return 0 #placeholder


if __name__=='__main__':
   baseURL = 'http://en.wikipedia.org'
   startingURL = baseURL + '/wiki/Outline_of_calculus'
   threadWords = ['Math','Mathematics','math','mathematics']
   filters = [lambda x: x, # eliminates None types - must always be first filter
              lambda x: x.startswith('/wiki'), # only keep other wikipedia links
              lambda x: x.count(':') == 0, # exclude templates
              lambda x: x.count('#') == 0] # exclude links to named sections
   
   myPot = Pot(startingURL,threadWords,filters)
   print myPot.links()

if False:
   spider = BreadthFirstSearch(startingURL)
   depth = 0
   
   #soup.body.h2.find_all_previous(text=threadWords)
   
   while len(spider) and depth < 3:
      url = next(spider)


   