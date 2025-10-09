#!/usr/bin/python3
####https://www.runoob.com/python/python-variable-types.html
#1 if-elseIf-else 
#2 "", '', 
#3 缩进相同的一组语句构成一个代码块，我们称之代码组。将首行及后面的代码组称为一个子句(clause)
#4 变量是存储在内存中的值，这就意味着在创建变量时会在内存中开辟一个空间。
#4.1 Python 中的变量赋值不需要类型声明。
#4.2 Python允许你同时为多个变量赋值。例如：a = b = c = 1
#4.3 Python有五个标准的数据类型：Numbers（数字）String（字符串）List（列表）Tuple（元组）Dictionary（字典）
#4.4 del语句删除单个或多个对象的引用。del var_a, var_b
#4.5 Python支持四种不同的数字类型：int（有符号整型）long（长整型，也可以代表八进制和十六进制）float（浮点型）complex（复数）
#4.5.1 长整型也可以使用小写 l，但是还是建议您使用大写 L，避免与数字 1 混淆。Python使用 L 来显示长整型。
#4.5.2 Python 还支持复数，复数由实数部分和虚数部分构成，可以用 a + bj,或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。
#4.6 (String)是由数字、字母、下划线组成的一串字符, python的字串列表有2种取值顺序:
#4.6.1 要实现从字符串中获取一段子字符串的话，可以使用 [头下标:尾下标] 来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
#4.6.2 加号（+）是字符串连接运算符，星号（*）是重复操作
#5 列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾
#6 元组是另一个数据类型，类似于 List（列表），不能更改。 类似于枚举列表。 元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表
#7 字典(dictionary)是 列表是有序的对象集合，字典是无序的对象集合.  ：字典当中的元素是通过键来存取的，而不是通过偏移存取。字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
#7.1 字典像 java 的map, javascript 的object
#8 Python 数据转换 只需要将数据类型作为函数名即可。
#9 Python 逻辑运算符 and , or ,not,  在java是$$ , ||, !,  javascript 是||（或），&&（与），!（非），??
#10 Python 成员运算符 in, not in, 
#11 Python 身份运算符 is ,is not is 是判断两个标识符是不是引用自一个对象。 （is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。）


days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

#first sentence 
if True: 
    print("lalal1 true")
elif False:
    print("lalala real false")
else:
    print("lala false")


#变量
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串


print("--------" + "Variable " + "------") 
print (counter)
print (miles)
print (name)

#String 
StringTest = "abcdefg"
print("--------" + "String " + "------")
print(StringTest[0:4]) #abcd
print(StringTest[2:])  #cdefg
print(StringTest *3) #abcdefgabcdefgabcdefg
print(StringTest + "test")  #abcdefgtest

#List
list1 = ['a','b','c','d','e','g']
tinylist = [123, 'john']
print("--------" + "List " + "------")
print(list1[:])  #['a', 'b', 'c', 'd', 'e', 'g']
print(list1[1])  # b
print(list1[1:4]) # ['b', 'c', 'd']
print( tinylist * 2 )      # 输出列表两次
print( list1 + tinylist)    # 打印组合的列表   ['a', 'b', 'c', 'd', 'e', 'g', 123, 'john']
print(list1[2:5:2])  #列表截取可以接收第三个参数，参数作用是截取的步长  ['c', 'e']

#Tuple 元组
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print("--------" + "Tuple " + "------")
print (tuple)               # 输出完整元组
print (tuple[0])            # 输出元组的第一个元素
print (tuple[1:3] )         # 输出第二个至第四个（不包含）的元素 
print (tuple[2:] )          # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2 )      # 输出元组两次
print (tuple + tinytuple)   # 打印组合的元组

#dictionary 字典
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}

print("--------" + "dictionary " + "------")
print (dict['one'])          # 输出键为'one' 的值
print (dict[2] )             # 输出键为 2 的值
print (tinydict)             # 输出完整的字典
print (tinydict.keys())      # 输出所有键
print (tinydict.values() )   # 输出所有值
print (tinydict["name"] )    # 输出"name" 的vaue runoob
list2=[]
for key in tinydict:
    print(f"key: {key}")     # 遍历key key: name key: code key: dept
    list2.append(key)
    value = tinydict[key]
    print(f"value: {value}")     # 遍历key key: name key: code key: dept
print(list2)
print(tinydict[list2[2]])  # 用list 查询direction
print(set(tinydict.keys())) #
print(set)

# key2 = list2[1]
# print(key2)

#类型转换 
print("--------" + "data type conversion " + "------")
stringConvert = "abcdefghijk"
n=81
eval("n + 4")
print(eval("n + 4"))  #85

#运算符 
print("--------" + "运算符 " + "------")
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
 
if ( a in list ):
   print (f"1 - 变量 {a} 在给定的列表中 list 中")
else:
   print (f"1 - 变量 {a} 不在给定的列表中 list 中")

if ( a is b ):
   print (f"3 - {a} 和 {b} 有相同的标识")
else:
   print (f"3 - {a} 和 {b} 没有相同的标识")