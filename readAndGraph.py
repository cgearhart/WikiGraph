
import urllib2
from bs4 import BeautifulSoup

class Pot(object):
   # Wrapper/helper class for BeautifulSoup
   
   def __init__(self,url,words,filters,verbose=False):
      self._url = url
      self._nodeWords = words
      self._filters = [lambda x: x] + filters # always want to filter None first
      self.links = None
      self.isNode = None
      self.soup = None
      self.refresh(verbose=verbose)
      
   def _makeSoup(self,verbose=False):
      # handle page request and convert page to soup
      botHeaders = {'User-Agent' : '628318'} # Tau FTW
      req = urllib2.Request(self._url, headers=botHeaders)
      pageHandle = urllib2.urlopen( req )
      self.soup = BeautifulSoup(pageHandle.read())
      if verbose:
         print '\nFinished the new batch of soup at url: {}\n'.format(self._url)
   
   def _getLinks(self,verbose=False):
      ''' 
      '''
      a_tags = self.soup.find_all('a')
      links = [(tag.get('href'),tag.get_text()) for tag in a_tags] 
      
      for test in self._filters:
         if verbose:
            oldlinks = links[:]
         links = [link for link in links if test(link[0])]
         if verbose:
            print '\n\n\nfilter removed-----------------------------'
            linksdiff = set(oldlinks) - set(links)
            for link in linksdiff:
               print link
      self.links = links
   
   def _isNode(self,verbose=False):
      ''' Tests whether the current URL should be considered a node.
      
      The current URL is a node if one of the paragraphs before the TOC contains 
      any of the words in self._nodeWords.
      '''
      #bodyContentTag = self.soup.find(id='bodyContent')
      self.isNode = False
      for paragraph in self.soup.h2.find_all_previous('p'):
         if paragraph.find(text=self._nodeWords):
            self.isNode = True
            if verbose:
               print '\n{} is a node.\n'.format(self._url)
      
   def refresh(self,url=None,filters=None,nodeWords=None,verbose=False):
      # Force a refresh of the object state
      if verbose:
         print 'Forcing Pot refresh.'
      if url:
         print 'URL changed from {} to {}'.format(self._url,url)
         self._url = url
      if filters:
         print 'The filters changed.'
      self._filters[1:] = filters
      if nodeWords:
         print ('The key words defining graph edges have been changed from {} '
                'to {}'.format(self._nodeWords,nodeWords)
               )
         self._nodeWords = nodeWords
      self._makeSoup(verbose)  # update the soup 
      self._getLinks(verbose)  # refresh the links
      self._isNode(verbose)   # determine if the URL is a node
      

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
      
      print 'Attempting to use URL: {}\n'.format(startingURL)
      
      if myPot.isNode:
         print '\n{} is a node!!!\n'.format(startingURL)
         
         for link in myPot.links:
            print link
            
      else:
         print '\n{} is NOT a node!!!\n'.format(startingURL)

   print '#### LET\'S TRY CHANGING THINGS FOR A SINGLE INSTANCE'

   url = baseURL + testURLs[0]
   testPot = Pot(url,threadWords,filters,verbose=True)

   print '## FORCE REFRESH'

   testPot.refresh(verbose=True)
   print '\nFinished force refresh\n'

   print '## URL'

   newURL = baseURL + testURLs[1]
   testPot.refresh(newURL,verbose=True)
   print '\nChanged the URL\n'
   
   print '## NODE WORDS'
   words = ['Matt']
   testPot.refresh(nodeWords=words,verbose=True) # this should break things
   print '\nThis should say False: {}'.format(testPot.isNode)
   testPot.nodeWords = threadWords

   print '## FILTERS'

   filters = [lambda x: not x] # should return zero links - might break things
   testPot.refresh(filters=filters,verbose=True)
   testLinks = [link for link in testPot.links]
   if not testLinks:
      print '\nAll links removed.\n'
   print '\nBroke the links (hopefully) by removing them all.\n'


