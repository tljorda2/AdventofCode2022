#%%
# I use this to test the runtime as part of the goal for this project is to minimize its runtime
# All files have to be in the same directory
import time

startMillis = int(round(time.time() * 1000))
print (startMillis)

import AdventofCode_Day1
import AdventofCode_Day2
import AdventofCode_Day3
import AdventofCode_Day4
import AdventofCode_Day5

endMillis = int(round(time.time() * 1000))
print (endMillis)
timeTaken = endMillis - startMillis
print(timeTaken)
#%%

# %%
