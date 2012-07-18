
################################################################################
#                                                                              #
# Exception Formatting                                                         #
#                                                                              #
# Source: SO - question/666022                                                 #
#                                                                              #
################################################################################

r"""
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
   print formatExceptionInfo()
"""
########################### END OF EXCEPTION TRACING ###########################


################################################################################
#                                                                              #
# Alternative to lambda test definitions                                       #
#                                                                              #
#                                                                              #
#                                                                              #
################################################################################

r"""
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

"""
########################### END OF LAMBDA ALTERNATIVE ##########################
