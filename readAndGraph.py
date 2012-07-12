import urllib2
from bs4 import BeautifulSoup

class Pot():
   
   def __init__(self,url,words):
      self.threadWords = words
      self.soup = self.makeSoup(self,url)
      
   def makeSoup(self,url):
      self.soup
      
   def get_links(self):
   
   def validityTest(self,**kargs):
      for arg in 
      
      

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
   startingURL = 'http:' + '//en.wikipedia.org/wiki/Outline_of_calculus'
   threadWords = ['Math','Mathematics','math','mathematics']
   depth = 0
   
   spider = BreadthFirstSearch(startingURL)

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
   