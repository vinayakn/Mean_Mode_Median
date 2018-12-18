## Mean_Mode_Median

## Module To Get Mean Mode Median of Array

# Clone or Download  https://github.com/vinayakn/Mean_Mode_Median.git

unzip and store file at required location(same location where you python/notebook is running)

Then run this code from terminal or any notebook 

------------------------------------------------------------------------------------------------------------------------------------
from  BASIC_STAT import get as Basic;

d=Basic.Stats([10,20,25,50,35,40]);

print d.mean();

print d.median();

print d.mode();

Results:

Mean of Data : 30.0

Median of Data : 30.0

There is no mode for this data set. All values occur only once.


--------------------------------------------------------------------------------------------------------------------------------------

from  BASIC_STAT import get as Basic;

d=Basic.Stats([10,20,25,50,35,40,500]);

print d.mean();

print d.median();

print d.mode();

Result:

Mean of Data : 97.0

Median of Data : 35

There is no mode for this data set. All values occur only once.
