# Mean_Mode_Median

Say we have collected some data that may be in any random domain for example in Retail domain the Sales data,or may be in Online Advertising domain the Campaign data(How many Impression served/CTR/CPM etc) or say in Automobile Domain the Production data(Number of cars manufactured). It may be any data in any domain if we would like to summaries or describe the data with single value as a starting point then how we can do it? this is when Measure of central tendency comes into picture. 

**Let’s go over below most common Measure of Central Tendency .**
* Mean
* Median
* Mode

To understand what is mean median and Mode do go through this article at [Median](https://medium.com/@vinayak_navale/mean-mode-median-measure-of-central-tendency-cf996948fc3f) and feel free to share and clap :)


Package to find Mean mode and Median of an Array

## Installation
requre python 2.7

## Steps to Follow.
-----------------------------------------------------------------------------------------------------------------------------------
1. [Click here to Clone or Download](https://github.com/vinayakn/Mean_Mode_Median.git)

2. Unzip the fild downloaded or cloned and store file at required location(same location where you python/notebook is running)

3. Then run this code from terminal or any notebook 
------------------------------------------------------------------------------------------------------------------------------------

## How to Use?:<br /> 

#### Example 1:<br /> 

* **importing file**<br /> 
From  BASIC_STAT import get as Basic;<br /> 

* **calculating Mean Mode and Median of any array:**<br />
 d=Basic.Stats([10,20,25,50,35,40]);<br /> 
 print d.mean();<br /> 
 print d.median();<br /> 
 print d.mode();<br /> 

* **Results:**<br /> 
Mean of Data : 30.0<br /> 
Median of Data : 30.0<br /> 
There is no mode for this data set. All values occur only once.<br /> 


--------------------------------------------------------------------------------------------------------------------------------------

#### Example 2:<br /> 

* **importing file**<br /> 
From  BASIC_STAT import get as Basic;<br /> 

* **Calulating Mean Mode Median of any array:**<br />
d=Basic.Stats([10,20,25,50,35,40,500]);<br /> 
print d.mean();<br /> 
print d.median();<br /> 
print d.mode();<br /> 

* **Result:**<br /> 
Mean of Data : 97.0<br /> 
Median of Data : 35<br /> 
There is no mode for this data set. All values occur only once.<br /> 

---------------------------------------------------------------------------------------------------------------------------------------

#### Example 3:<br /> 

* **importing file**<br /> 
From  BASIC_STAT import get as Basic<br /> 

* **Calulating Mean Mode Median of any array:**<br /> 
d=Basic.Stats([10,20,25,50,35,40,40,40,40]);<br /> 
print d.mean();<br /> 
print d.median();<br /> 
print d.mode();<br /> 

* **Result:**
Mean of Data : 33.0<br /> 
Median of Data : 40<br /> 
Mode of Data : [40]  Freq: 4<br /> 
