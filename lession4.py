## https://www.runoob.com/python/python-modules.html
#1 模块能定义函数，类和变量，模块里也能包含可执行的代码
#2 #globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字, 名字们能用 keys() 函数摘取
#3 用 reload() 函数。该函数会重新导入之前导入过的模块
#4 包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__init__.py 用于标识当前文件夹是一个包

import math
import lession3, lesson1
from lesson1 import days
from lession3 import printme,printinfo,sum
from lession3 import *
from libPackage.runoob1 import runoob1
from libPackage.runoob2 import runoob2

print("--------" + "Module " + "------")
lession3.printme(days)
print ("相加后的值为 : ", sum( 10, 20 ))

#dir() 
print("--------" + "dir() " + "------")
#dir(),  __name__指向模块的名字，__file__指向该模块的导入文件名
content = dir(math)
 
print (content)
print(dir(math)[2])

#package 
print("--------" + "globals, local space " + "------")
print(globals().keys())

#package 
print("--------" + "Lib and Package " + "------")
runoob1()
runoob2()








