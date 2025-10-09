## https://www.runoob.com/python/python-functions.html
#1 函数
#1.1 python 函数的参数传递：
#1.1.1 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
#1.1.2 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
#1.1.3 python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
#2 函数时可使用的正式参数类型：必备参数 关键字参数 默认参数 不定长参数
#2.1 匿名函数lambda只是一个表达式，函数体比def简单很多。, python 使用 lambda 来创建匿名函数。 
#2.1.1 lambda只是一个表达式，函数体比def简单很多。
#2.1.2 lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
#2.1.3 lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
#2.1.4 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
#3 return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
#4 全局变量和局部变量 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。

def printme( str ):
   "打印传入的字符串到标准显示设备上"
   print (str)
   return

# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")

## 可变参数
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)

## 不可变参数
def ChangeInt( a ):
    a = 10
    print(f"函数内 {a}")
 
b = 2
ChangeInt(b)
print (f"函数外 {b}") # 结果是 2


#关键字参数
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("Name: ", name)
   print ("Age ", age)
   return
 
printinfo( age=50, name="miki" )

#默认参数
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("Name: ", name)
   print ("Age ", age)
   return
 
printinfo( age=50, name="miki" )
printinfo( name="miki" )

#不定长参数
print("--------" + "不定长参数 " + "------")
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )

#lambda
print("--------" + "匿名函数lambda " + "------")
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))