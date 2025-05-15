
import numpy as np
x = np.random.rand(5);

try:
  print(x)
  print('---------------------------------')
  
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


print('---------------------------------')
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")