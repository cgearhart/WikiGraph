import urllib2
from bs4 import BeautifulSoup

baseURL = 'http://en.wikipedia.org'
startingURL = baseURL + '/wiki/calculus'
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
print soup.body.h2.find_all_previous(text=threadWords)


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