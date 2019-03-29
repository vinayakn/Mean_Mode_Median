# Mean_Mode_Median

##Package to find Mean mode and Median of an Array

## Installtion
requre python 2.7

## Steps to Follow.
-----------------------------------------------------------------------------------------------------------------------------------
1. [Click here to Clone or Download[(https://github.com/vinayakn/Mean_Mode_Median.git)

2. unzip the fild downloaded or cloned and store file at required location(same location where you python/notebook is running)

3. Then run this code from terminal or any notebook 
------------------------------------------------------------------------------------------------------------------------------------

## How to Use?:

#### Example 1:

**importing file**
>> From  BASIC_STAT import get as Basic;

**calculating Mean Mode and Median of any array:**
>> d=Basic.Stats([10,20,25,50,35,40]);
>> print d.mean();
>> print d.median();
>> print d.mode();

**Results:**
Mean of Data : 30.0
Median of Data : 30.0
There is no mode for this data set. All values occur only once.


--------------------------------------------------------------------------------------------------------------------------------------

#### Example 2:

**importing file**
>>From  BASIC_STAT import get as Basic;

**Calulating Mean Mode Median of any array:**
>>d=Basic.Stats([10,20,25,50,35,40,500]);
>>print d.mean();
>>print d.median();
>>print d.mode();

**Result:**
Mean of Data : 97.0
Median of Data : 35
There is no mode for this data set. All values occur only once.

---------------------------------------------------------------------------------------------------------------------------------------

#### Example 3:

**importing file**
>>From  BASIC_STAT import get as Basic

**Calulating Mean Mode Median of any array:**
>>d=Basic.Stats([10,20,25,50,35,40,40,40,40])
>>print d.mean()
>>print d.median()
>>print d.mode()

**Result:**
Mean of Data : 33.0
Median of Data : 40
Mode of Data : [40]  Freq: 4
