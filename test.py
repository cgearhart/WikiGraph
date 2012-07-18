
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