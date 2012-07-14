
import urllib2
from bs4 import BeautifulSoup

class Pot():
   # Wrapper/helper class for BeautifulSoup - also a graphObj for search
   
   def __init__(self,words,filters,baseURL=None):
      self._baseURL = baseURL
      self._nodeWords = words
      self._filters = [lambda x: x] + filters # always want to filter None first
      self._url = None
      self.node = None
      self.links = None
      self.isAtNode = None
      self.soup = None
      
   def _makeSoup(self,verbose=False):
      # handle page request and convert page to soup
      
      # TODO: Figure out why /wiki/chain_rule breaks the parser (not a BS bug)
      botHeaders = {'User-Agent' : '628318'} # Tau FTW
      req = urllib2.Request(self._url, headers=botHeaders)
      pageHandle = urllib2.urlopen( req )
      try:
         self.soup = BeautifulSoup(pageHandle.read())
         if verbose:
            print '\nFinished the new batch of soup at url: {}\n'.format(self._url)
      except:
         print '_makeSoup() error!'
         print self.node
   
   def _getLinks(self,verbose=False):
      # make a list of all links found at the target URL
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
      self.isAtNode = False
      headingTag = self.soup.h2
      
      # TODO: some pages don't have enough content to have <h2>; this should
      # be modified to handle those cases more elegantly (like "if no h2, search all")
      try: 
         if headingTag:
            for paragraph in headingTag.find_all_previous('p'):
               if paragraph.find(text=self._nodeWords):
                  self.isAtNode = True
                  if verbose:
                     print '\n{} is a node.\n'.format(self._url)
      except AttributeError:
         print 'Error!'
         print 'Node: {}'.format(self.node)
               
   def moveTo(self,linkTuple):
      self.refresh(linkTuple=linkTuple)
      
   def refresh(self,filters=None,nodeWords=None,linkTuple=None,verbose=False):
      # Force a refresh of the object state
      if verbose:
         print 'Forcing Pot refresh.'
      if linkTuple:
         if verbose:
            print 'Updating the URL from the link tuple'
         self.node = linkTuple
         self._url = self._baseURL + str(linkTuple[0])
               
      else:
         if filters:
            if verbose:
               print 'The filters changed.'
            self._filters[1:] = filters
         if nodeWords:
            if verbose:
               print ('The key words defining graph edges have been changed from {} '
                      'to {}'.format(self._nodeWords,nodeWords)
                     )
            self._nodeWords = nodeWords
         
      self._makeSoup(verbose)  # update the soup 
      self._getLinks(verbose)  # refresh the links
      self._isNode(verbose)   # determine if the URL is a node
      

class DepthLimitedBFS():
   
   def __init__(self,graphObj,startingNode,depthLimit=1):
      self._stack = [startingNode]
      self._nextLayerStack = []
      self._graphObj = graphObj
      self.depthLimit = depthLimit
      self.visited = {}
      self.graph = {}
      self.depth = 0
      
   def search(self,verbose=False):
      while self._stack and self.depth <= self.depthLimit:
         possibleNode = self._stack.pop(0)
         if possibleNode not in self.visited:
            self.visited[possibleNode] = None
            self._graphObj.moveTo(possibleNode)
            if self._graphObj.isAtNode:
               links = self._graphObj.links
               self.graph[possibleNode] = links
               self._nextLayerStack.extend(links)
            
               if verbose:
                  print 'New node: {}\n'.format(possibleNode)
            elif verbose:
               print 'Not added: {}\n'.format(possibleNode)
               
         elif verbose:
            print 'Repeat node: {}\n'.format(possibleNode)
         
         if not self._stack and self._nextLayerStack:
            self._nextLayerStack = list(set(self._nextLayerStack))
            print r'###### End of layer {} ######'.format(self.depth)
            print r'###### Links in next layer: {} ######\n'.format(len(self._nextLayerStack))
            self._stack.extend(self._nextLayerStack)
            self._nextLayerStack = []
            self.depth += 1


class Gephi():

   def __init__(self,inputDict):
      self.data = inputDict
      
   def asCSV(self):
      return 0 #placeholder
      
def testSearcher(verbose=False):
   baseURL = 'http://en.wikipedia.org'
   threadWords = ['Math','Mathematics','math','mathematics']
   
   filters = [lambda x: x.startswith('/wiki'), # only keep other wikipedia links, and exclude foreign languages
              lambda x: x.count(':') == 0, # exclude templates
              lambda x: x.count('#') == 0, # exclude links to named sections
              lambda x: not x.endswith('(disambiguation)') # obvious
             ]
             
   testURL = '/wiki/Outline_of_calculus'
   
   myPot = Pot(threadWords,filters,baseURL)   
   startingTuple = (testURL, 'Outline of Calculus')
   nodeSearcher = DepthLimitedBFS(myPot,startingTuple)
   nodeSearcher.search(verbose=verbose)
   
   print 'Test graph:\n'
   for key,value in nodeSearcher.graph.iteritems():
      print "\nNode: {}\n".format(key)
      print "Edges:"
      for thing in value:
         print '\t{}'.format(thing)
      

def testPot():
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


if __name__=='__main__':

   testSearcher(verbose=True)

   


   
   
   
      