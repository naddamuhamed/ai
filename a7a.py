import numpy as np

x=[['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
['|',' ',' ','_',' ','|',' ','|','_',' ','|','_',' ','|',' ',' ','|'],
['|',' ','|','_','_','|','_',' ','|','_','_',' ','|','_','|',' ','|'],
['|',' ',' ',' ','_','_',' ',' ',' ','|',' ','_','_','|',' ','_','|'],
['|',' ',' ','|',' ','_','|',' ','|','_','_','_','_',' ','|',' ','|'],
['|',' ',' ','_','_','|',' ','_',' ','|','_','_',' ','|','_',' ','|'],
['|',' ',' ','|','_',' ','|','_',' ','|',' ','_','|',' ','|',' ','|'],
['|',' ',' ','|','_','_','_','|',' ','|','_','_','|',' ','_','_','|'],
['|',' ',' ','_',' ','|',' ','_','_','|','_',' ','|','_','_',' ','|'],
['|',' ','_','|',' ','_','|',' ',' ','|',' ','|',' ','_','|',' ','|'],
['|','_','_','_','_','_','_','_','_','|','_','_','|','_','_','_','|']]
# print(x)
for r in x:
   for c in r:
      print(c,end = "")
   print()