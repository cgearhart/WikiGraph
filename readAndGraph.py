
import urllib2
from bs4 import BeautifulSoup

class Pot(object):
   # Wrapper/helper class for BeautifulSoup
   
   def __init__(self,url,words,filters,verbose=False):
      self._url = url
      self._nodeWords = words
      self._filters = [lambda x: x] + filters # always want to filter None first
      self._links = None
      self.isNode = None
      self.soup = None
      self.verbose = verbose
      self.refresh()
      
   def __iter__(self):
      return self.next()
      
   def next(self):
      for link in self._links:
         yield link
      
   def _makeSoup(self):
      # handle page request and convert page to soup
      botHeaders = {'User-Agent' : '628318'} # Tau FTW
      req = urllib2.Request(self._url, headers=botHeaders)
      pageHandle = urllib2.urlopen( req )
      self.soup = BeautifulSoup(pageHandle.read())
      if self.verbose:
         print '\nFinished the new batch of soup at url: {}\n'.format(self._url)
   
   def _getLinks(self):
      ''' 
      '''
      a_tags = self.soup.find_all('a')
      links = [(tag.get('href'),tag.get_text()) for tag in a_tags] 
      
      for test in self._filters:
         if self.verbose:
            oldlinks = links[:]
         links = [link for link in links if test(link[0])]
         if self.verbose:
            print '\n\n\nfilter removed-----------------------------'
            linksdiff = set(oldlinks) - set(links)
            for link in linksdiff:
               print link
      self._links = links
   
   def _isNode(self):
      ''' Tests whether the current URL should be considered a node.
      
      The current URL is a node if one of the paragraphs before the TOC contains 
      any of the words in self._nodeWords.
      '''
      bodyContentTag = self.soup.find(id='bodyContent')
      for paragraph in bodyContentTag.h2.find_all_previous('p'):
         if paragraph.find(text=self._nodeWords):
            self.isNode = True
            if self.verbose:
               print '\n{} is a node.\n'.format(self._url)
            return
      self.isNode = False
   
   @property
   def nodeWords(self):
      return self._nodeWords
   
   @nodeWords.setter
   def nodeWords(self,newWords):
      # Change the words that indicate this URL as a node
      self._nodeWords = newWords
      self._isNode()
   
   @property
   def url(self):
      return self._url
   
   @url.setter
   def url(self,newURL):
      # Change the target URL
      print 'I got called!'
      self._url = newURL
      self.refresh() # Refresh everything if the target URL changes
   
   @property
   def filters(self):
      return self._filters
      
   @filters.setter
   def filters(self,newFilters):
      # Change the filters used on page links
      self._filters[1:] = newFilters # Don't allow the 'None' test to be changed
      self._getLinks() # Re-filter the links if the filters are changed
      
   def refresh(self):
      # Force a refresh of the object state
      if self.verbose:
         print 'Forcing Pot refresh of URL: {}'.format(self._url)
      self._makeSoup()
      self._getLinks()
      self._isNode()
      

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
   threadWords = ['Math','Mathematics','math','mathematics']
   
   filters = [lambda x: x.startswith('/wiki'), # only keep other wikipedia links, and exclude foreign languages
              lambda x: x.count(':') == 0, # exclude templates
              lambda x: x.count('#') == 0, # exclude links to named sections
              lambda x: not x.endswith('(disambiguation)') # obvious
              ]
   
   testURLs =  ['/wiki/Outline_of_calculus', # is a node
                '/wiki/Calculus',   # is a node
                '/wiki/Art'   # is NOT a node
                ]
   
   
   print '##################### LET\'S TRY TESTING ##################'

   for tURL in testURLs:
      startingURL = baseURL + tURL
      myPot = Pot(startingURL,threadWords,filters,verbose=False)
      
      generatorWorked = False # Haven't tried yet
      
      print 'Attempting to use URL: {}\n'.format(startingURL)
      
      if myPot.isNode:
         print '\n{} is a node!!!\n'.format(startingURL)
         
         for link in myPot:
            generatorWorked = True
            print link
            
         if generatorWorked:
            print '\nmyPot is a generator!!!\n'
      else:
         print '\n{} is NOT a node!!!\n'.format(startingURL)

   print '#### LET\'S TRY CHANGING THINGS FOR A SINGLE INSTANCE'

   url = baseURL + testURLs[0]
   testPot = Pot(url,threadWords,filters,verbose=True)

   print '## FORCE REFRESH'

   testPot.refresh()
   print '\nFinished force refresh\n'

   print '## URL'

   print baseURL + testURLs[1]
   testPot.url = baseURL + testURLs[1]
   print testPot._url
   print '\nChanged the URL\n'
   
   print '## NODE WORDS'

   testPot.nodeWords = ['Matt'] # this should break things
   print '\nThis should say False: {}'.format(testPot.isNode)
   testPot.nodeWords = threadWords

   print '## FILTERS'

   testPot.filters = [lambda x: not x] # should return zero links - might break things
   testLinks = [link for link in testPot]
   if not testLinks:
      print '\nAll links removed.\n'
   print '\nBroke the links (hopefully) by removing them all.\n'


