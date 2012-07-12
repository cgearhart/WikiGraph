class Thing():

   def __init__(self):
      self.thing = []
      
   def pop(self):
      topThing = self.thing.pop()
      return topThing
      
   def append(self,stuff):
      self.thing.append(stuff)
      
   def __len__(self):
      return len(self.thing)
      
   def __str__(self):
      return repr(self.thing)
      
   def __iter__(self):
      return self
      
   def next(self):
      return self.pop()
      

aThing = Thing()

aThing.append(10)

stop = 10

for thing in aThing:
   print thing
   print aThing
   aThing.pop()
   stop -= 1
   if stop > 3:
      aThing.append(stop)
   print aThing