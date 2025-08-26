#import pandas
#pandas.read_csv()#read r the fns
import math
result=math.sqrt(3)
print(result)
#by using from keyword
from math import sqrt,pi
result=sqrt(9)*pi
print(result)
#by using * import everything,but not recommanded
#by using as keyword as short form
from math import sqrt as s
import math as m
result=m.sqrt(9)#here name.fn r method is imp
print(result)
#dir fn by this we can view name of all fntns n variables defined in the module
import math
print(dir(math))
print(math.pi,type(math.pi))#to know the type of pi

