import urllib2
from bs4 import BeautifulSoup

class Pot():
   
   def __init__(self,url,words,filters=lambda x: x):
      self.threadWords = words
      self.filters = filters
      self.soup = self.makeSoup(self,url)
      
   def makeSoup(self,url):
      botHeaders = {'User-Agent' : '628318'} # Tau FTW
      req = urllib2.Request(url, headers=botHeaders)
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
   baseURL = 'http://en.wikipedia.org'
   startingURL = baseURL + '/wiki/Outline_of_calculus'
   threadWords = ['Math','Mathematics','math','mathematics']
   filters = [lambda x: x,
              lambda x: x.startswith('/wiki'),
              lambda x: x.count(':'),
              lambda x: x.count('#')]
   
   myPot = Pot(startingURL,threadWords,filters)
   spider = BreadthFirstSearch(startingURL)
   depth = 0
   
   while len(spider) and depth < 3;
      url = next(spider)

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
   