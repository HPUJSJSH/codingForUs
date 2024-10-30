## 1.Python基本语句(上)

### 注释

---

 什么是注释，注释相当于备注的信息，也可以在调试代码的时候隐藏执行代码。

  注释的方法有**行注释**和**块注释**。

#### 行注释

行注释以 **#** 开头：

```python
# 实例 1
# 这是行注释
```

#### 块注释

块注释可以用多个 **#** 、 **三单引号**或**三双引号**：

​	

```python
# 实例 2
# 这
# 是
# 块
# 注
# 释
```

```
# 实例 3
'''
这
是
块
注
释
'''
```

```
# 实例 4
"""
这
是
块
注
释
"""
```

### 输出语句

​    对于大多数程序语言，第一个入门编程代码便是 “Hello World！”。

```*# 实例 5* print("Hello, World!")
# 实例 5
 print("Hello, World!")
```

#### 举一反三

​    接下来我们试试输出"学习python的第一天！"。

```
 # 练习 1
 print("学习Python的第一天!")
```

### 标识符

1. 第一个字符必须是字母表中字母或下划线 _ 。
2. 标识符的其他的部分由字母、数字和下划线组成。
3. 标识符对大小写敏感。

​    标识符也叫变量名，变量名就是一个变量的名字，例如a和b。

​    a问b中午吃什么？

```
# 实例 7
 b="中午吃面条"
 print(b)
```

#### 举一反三

​    接下来我们试试使用 **换行符：/n**和**连字符：+** 输出a和b的对话

```python
# 练习 2
a="中午吃什么？\n"
b="中午吃面条"
print("a:"+a+"b:"+b)
```

### 多行语句

​    在编写代码中通常是一行写完一条语句，但如果变量名很长，我们可以使用反斜杠 \ 来实现多行语句在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \ ，例如：

```
# 实例 8
text1="明天天气"
text2="怎么样，是晴天"
text3= "还是雨天?"
print(text1+ \
      text2+ \
      text3)
```

```
# 实例 9
text1="明天天气"
text2="怎么样，是晴天"
text3= "还是雨天?"
list=[text1+text2+text3]
print(list)
```

## 2.Python基本语句(上)

### 行与缩进

​    python最具特色的就是使用缩进来表示代码块。

正确写法：

```python
# 实例 1
if True:
    print("True")
else:
    print("False") 
```

 若没有缩进则报错，或者缩进不规范也容易没有产生值。

错误写法：

```python
# 实例 2
if True:
print("True")
else:
print("False")
```

### 关键字

​        关键字指的是具有特殊功能的标识符。

关键字有：

```
False      class      finally    is         return

None       continue   for        lambda     try

True       def        from       nonlocal   while

and        del        global     not        with 

as         elif       if         or         yield

assert     else       import     pass

break      except     in         raise
```



跟java等语言一样，在python中有33个关键字，注意在python中，False、None和True的首字母大写，其他关键字全部小写。

### 数据类型
​        python的数据类型有：字符串、整型、列表、元组、字典、布尔型等等。数据类型是编程语言必备的属性，只有给数据赋予明确的数据类型，计算机才能对数据进行处理运算。

整数类型（int）简称整型，它用于表示整数。
        接下来看看整型是怎么表示的

```
# 实例 3      两种写法均可
counter = 100 # 赋值整型变量
counter = int(100)# 赋值整型变量
```

浮点型（Float）数学中的小数，用于表示实数。

接下来看看浮点型是怎么表示的

```python
# 实例 4      两种写法均可
miles = 1000.0 # 赋值浮点型变量
miles = float(100)# 赋值浮点型变量
```

字符串型（str）可以理解为中文

 比如"123"是**一二三**不是整型的**一百二十三**，接下来看看字符串型是怎么表示的

```
# 实例 5      三种写法均可
name = '100' # 赋值字符串型变量
name = "100" # 赋值字符串型变量
name = str(100)# 赋值字符串型变量
```

"“与’‘区别：
    ""优先级比’'大也可以理解为”"里面用’’

```python
# 实例 6      
name = "'中国'+'中华'"
```

布尔型是整型的子类型，布尔型数据只有两个取值：True和False，分别对应整型的1和0。

#### 比较运算：

1. 等于 == 不等于 ！=
2. 小于等于 <= 大于等于>=
3. 大于 > 小于 <

#### 逻辑运算

1. 与运算 and 一假则假
2. 或运算 or 一真则真
3. 非运算 not 真假倒转

```
# 实例 6      
a = True
print(a and 0 or 99) # ==> 99
```

## 3.import导包（库）和Python条件语句

### 导入包（库）

在 python 用 import 或者 from…import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *

将某个模块改名(改为s)，格式为：import somemodule as s


```
# 实例 1
import sys 
print('================Python import mode==========================') 
print ('命令行参数为:') 
for i in sys.argv: 
    print (i) 
    print ('\n python 路径为',sys.path)
```

### if 判断条件

if：

​    执行语句……

条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。

```
# 实例 2
a=0
b=1
if a>b: 
    print(a,">",b)
```

### if else分支语句

if：

​    执行语句……

else：

​    执行语句……

程序语言指定任何非0和非空（null）值为true，0 或者 null为false。

编程中 if 语句用于控制程序的执行，基本形式为：

```
# 实例 3
a=1
b=0
if a>b: 
    print(a,">",b)
else: 
    print(a,"<",b)
```

其中"判断条件"成立时（非零），则执行后面的语句，而执行内容可以多行，以缩进来区分表示同一范围。else 为可选语句，当需要在条件不成立时执行内容则可以执行相关语句。

### if elif else多分支语句

if：

执行语句……

elif： 

执行语句……

else： 

执行语句……

if 语句的判断条件可以用>（大于）、<(小于)、==（等于）、>=（大于等于）、<=（小于等于）来表示其关系。

当判断条件为多个值时，可以使用以下形式：


```
# 实例 4
num = 5 
if num == 3:# 判断num的值 
    print 'boss' 
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0: # 值小于零时输出
    print 'error' 
else: 
    print 'roadman' # 条件均不成立时输出
```

​	由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。

​        当if有多个条件时可使用括号来区分判断的先后顺序，括号中的判断优先执行，此外 and 和 or 的优先级低于>（大于）、<（小于）等判断符号，即大于和小于在没有括号的情况下会比与或要优先判断。

简单的语句组

你也可以在同一行的位置上使用if条件判断语句，如下实例：

```
# 实例 5
var = 100 
if ( var == 100 ) :print "变量 var 的值为100"
    
print "Good bye!"

```

## 4.Python循环语句

编程语言提供了各种控制结构，允许更复杂的执行路径。

循环语句允许我们执行一个语句或语句组多次，下面是在大多数编程语言中的循环语句的一般形式：

### While 循环语句

while 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。

```
# 实例 1
count = 0 
while (count < 9): 
    print('The count is:', count)
    count = count + 1
print("Good bye!")
```

### While 循环语句 else

while … else 在循环条件为 false 时执行 else 语句块：

```
# 实例 2
count = 0 
while count < 5:
    print(count, " is less than 5") 
    count = count + 1 
else:
    print(count, " is not less than 5")
```

### for 循环语句

for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

```
# 实例 3
for letter in 'Python': # 第一个实例 
    print("当前字母: %s" % letter) 
fruits = ['banana', 'apple', 'mango'] for fruit in fruits: # 第二个实例 
    print('当前水果: %s'% fruit) 
print("Good bye!")
```

### for 循环语句 else

在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。

```
# 实例 4
for num in range(10,20): # 迭代 10 到 20 之间的数字 
    for i in range(2,num): # 根据因子迭代 
        if num%i == 0: # 确定第一个因子 
        	j=num/i # 计算第二个因子 
        	print('%d 等于 %d * %d' % (num,i,j)) 
        	break # 跳出当前循环
    else: # 循环的 else 部分 
        print('%d 是一个质数' % num)

```

Python 循环嵌套
在一个循环体里面嵌入另一个循环。

while与while嵌套
for与for嵌套
你可以在循环体内嵌入其他的循环体，如在while循环中可以嵌入for循环， 反之，你可以在for循环中嵌入while循环。

以下实例使用了嵌套循环输出2~100之间的素数：


```
# 实例 5
i = 2
while(i < 100): 
    j = 2 
    while(j <= (i/j)):
        if i % j == 0:
            break
        j = j + 1
    else:
        print(i, " 是素数")
    i = i + 1 
print("Good bye!")

```

循环控制语句
循环控制语句可以更改语句执行的顺序。Python支持以下循环控制语句：

break 语句
Python break语句，就像在C语言中，打破了最小封闭for或while循环。

break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。

break语句用在while和for循环中。

如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。
```
# 实例 6
for letter in 'Python': # 第一个实例 
    if letter == 'h': 
        break 
    print('当前字母 :', letter)
print("Good bye!")
```

### continue 语句

Python continue 语句跳出本次循环，而break跳出整个循环。

continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。

continue语句用在while和for循环中。

```
# 实例 7
for letter in 'Python':# 第一个实例 
    if letter == 'h':
        continue 
    print('当前字母 :', letter)
print("Good bye!")
```

### pass 语句

Python pass 是空语句，是为了保持程序结构的完整性。

**pass** 不做任何事情，一般用做占位语句。

```
# 实例 8
for letter in 'Python':
    if letter == 'h':
        pass 
        print('这是 pass 块')
    print('当前字母 :', letter) 
print("Good bye!")
```

## 5.PythonNumber整数

在Python中，对象是数据的抽象表示，而引用则是指向对象的指针。Python中的所有事物都是对象，包括数字、字符串、函数等等。

引用是Python中的一种数据类型，它存储了对象的地址。当我们使用变量来存储对象时，实际上是将对象的地址存储在变量中，这个变量就是一个引用。

下面我们通过一个简单的例子来说明Python的对象和引用：
```
# 实例 1
a = 123
```

在这个例子中，我们定义了一个变量a，并将其赋值为整数123。实际上，a是一个引用，它存储了整数对象123的地址。

```python
# 实例 2
b = a
```

现在我们定义了另一个变量b，并将其赋值为变量a的值。由于a存储的是整数对象123的地址，因此b也存储了这个地址。因此，a和b引用了同一个对象。

```python
# 实例 3
del a
```

现在我们删除了变量a。由于a和b引用了同一个对象，因此Python并不会释放整数对象123所占用的内存。只有当没有任何引用指向这个对象时，Python才会释放它所占用的内存。

```python
# 实例 4
del b
```

现在我们删除了变量b。由于没有任何引用指向整数对象123，因此Python会释放它所占用的内存。

总而言之，Python中的对象是数据的抽象表示，而引用则是指向对象的指针。当我们使用变量来存储对象时，实际上是将对象的地址存储在变量中，这个变量就是一个引用。当我们删除一个变量时，Python会检查该变量是否有其他引用指向它所引用的对象。如果有其他引用指向该对象，则Python不会释放该对象所占用的内存，只有当没有任何引用指向该对象时，Python才会释放它所占用的内存。

Number(数字)
Python Number 数据类型用于存储数值。

数据类型是不允许改变的,这就意味着如果改变 Number 数据类型的值，将重新分配内存空间。

以下实例在变量赋值时 Number 对象将被创建：
```
# 实例 5
var1 = 5
var2 = 10
```

您也可以使用del语句删除一些 Number 对象引用。

del语句的语法是：

```python
# 实例 6
del var1[,var2[,var3[....,varN]]]]
```

您可以通过使用del语句删除单个或多个对象，例如：

```python
# 实例 7
del var
del var1,var2, ...... , varN
```

支持四种不同的数值类型：
整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。
长整型(long integers) - 无限大小的整数，整数最后是一个大写或小写的L。
浮点型(floating point real values) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
复数(complex numbers) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

```
int		long					float			complex
10		51924361L				0.0				3.14j
100		-0x19323L				15.20			45.j
-786	0122L					-21.9			9.322e-36j
080		0xDEFABCECBDAECBFBAEl	32.3+e18		.876j
-0490	535633629843L			-90.			-.6545+0J
-0x260	-052318172735L			-32.54e100		3e+26J
0x69	-4721885298529L			70.2-E12		4.53e-7j
```

- 长整型也可以使用小写"L"，但是还是建议您使用大写"L"，避免与数字"1"混淆。Python使用"L"来显示长整型。
- Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型

```
Number 类型转换
int(x [,base ])         将x转换为一个整数  
long(x [,base ])        将x转换为一个长整数  
float(x )               将x转换到一个浮点数  
complex(real [,imag ])  创建一个复数  
str(x )                 将对象 x 转换为字符串  
repr(x )                将对象 x 转换为表达式字符串  
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
tuple(s )               将序列 s 转换为一个元组  
list(s )                将序列 s 转换为一个列表  
chr(x )                 将一个整数转换为一个字符  
unichr(x )              将一个整数转换为Unicode字符  
ord(x )                 将一个字符转换为它的整数值  
hex(x )                 将一个整数转换为一个十六进制字符串  
oct(x )                 将一个整数转换为一个八进制字符串 

```

数学函数
函数	返回值 ( 描述 )

```
[abs(x)]	返回数字的绝对值，如abs(-10) 返回 10
[ceil(x)]	返回数字的上入整数，如math.ceil(4.1) 返回 5
[cmp(x, y)]	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
[exp(x)]	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
[fabs(x)]	返回数字的绝对值，如math.fabs(-10) 返回10.0
[floor(x)]	返回数字的下舍整数，如math.floor(4.9)返回 4
[log(x)]	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
[log10(x)]	返回以10为基数的x的对数，如math.log10(100)返回 2.0
[max(x1, x2,…)]	返回给定参数的最大值，参数可以为序列。
[min(x1, x2,…)]	返回给定参数的最小值，参数可以为序列。
[modf(x)]	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
[pow(x, y)]	x**y 运算后的值。
[round(x [,n])]	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
[sqrt(x)](	返回数字x的平方根
```

### 随机数函数

随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。

Python包含以下常用随机数函数：

```
函数	描述
[choice(seq)]	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
[randrange ([start,] stop [,step])]	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
[random()]	随机生成下一个实数，它在[0,1)范围内。
[seed([x])]	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
[shuffle(lst)]	将序列的所有元素随机排序
[uniform(x, y)]	随机生成下一个实数，它在[x,y]范围内。
```

### 三角函数

Python包括以下三角函数：

```
函数	描述
[acos(x)]	返回x的反余弦弧度值。
[asin(x)]	返回x的反正弦弧度值。
[atan(x)]	返回x的反正切弧度值。
[atan2(y, x)]	返回给定的 X 及 Y 坐标值的反正切值。
[cos(x)]	返回x的弧度的余弦值。
[hypot(x, y)]	返回欧几里德范数 sqrt(xx + yy)。
[sin(x)]	返回的x弧度的正弦值。
[tan(x)]	返回x弧度的正切值。
[degrees(x)]	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
[radians(x)]	将角度转换为弧度
```

### 数学常量

| 常量 | 描述                                  |
| ---- | ------------------------------------- |
| pi   | 数学常量 pi（圆周率，一般以π来表示）  |
| e    | 数学常量 e，e即自然常数（自然常数）。 |

## 6.访问字符串中的值
字符串
字符串是 Python 中最常用的数据类型。我们可以使用引号( ’ ’ 或 " " )来创建字符串。

创建字符串很简单，只要为变量分配一个值即可。

访问字符串中的值
Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。

Python 访问子字符串，可以使用方括号 [] 来截取字符串。


```
# 实例 1
var1 = 'Hello!'
var2 = "World!" 
print ("var1[0]: ", var1[0]) 
print ("var2[1:5]: ", var2[1:5])
```

#### 举一反三

接下来我们试试输出"Python"。

```python
# 练习 1
str1 = 'Is Python' 
print ("输出Python: ", str1[2:9]) 
```

### 字符串运算符

![image-20241030174322004](.\images\Snipaste_2024-10-30_17-45-37.png)

```
# 实例 2
a = "Python3.0"
b = "Python"
print("a + b 输出结果：", a + b) 
print("a * 2 输出结果：", a * 2) 
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
if( "H" in a) : 
    print("H 在变量 a 中") 
else : 
    print("H 不在变量 a 中") 
if( "M" not in a) : 
    print("M 不在变量 a 中") 
else :
    print("M 在变量 a 中")
print (r'\n')
print (R'\n')
```

### 字符串格式化

Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。

在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。

```
# 实例 3
print("今天学的是%s第%d天!" % ('Python', 6))
```

python字符串格式化符号:

![](.\images\Snipaste_2024-10-30_17-49-07.png)

## 7.列表

序列是 Python 中最基本的数据结构。

列表都可以进行的操作包括索引，切片，加，乘，检查成员。

创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。

### 列表数据类型

列表的数据项不需要具有相同的类型。

```
# 实例 1
List = ['a','b',1,2]
```

此外，Python 已经内置确定序列的长度以及确定最大和最小的元素的方法。

列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。

### 索引

序列中的每个值都有对应的位置值，称之为索引，第一个索引是 0，第二个索引是 1，索引也可以从尾部（负索引）开始，最后一个元素的索引为 -1，往前一位为 -2，以此类推。

```
# 实例 2
List = ['index1', 'index2', 'index3', 'index4', 'index5']
print("这是第一个索引",List[0])  
print("这是第二个索引",List[1])  
print("这是第三个索引",List[2])
print("这是倒数第一个索引",List[-1])  
print("这是倒数第二个",List[-2])  
print("这是倒数第三个",List[-3])
```

### 切片

使用下标索引来访问列表中的值，同样你也可以使用方括号 [ ] 的形式截取字符

接下来需要取列表1到10里面数的2到7之间的所有数

```python
# 实例 3
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
print(nums[1:7])
```

## 8.Python元组

元组与列表类似，不同之处在于元组的元素不能修改。

元组使用小括号 ( )，列表使用方括号 [ ]。

元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

### 索引
元组可以使用下标索引来访问元组中的值。

```
# 实例 1
tup1 = ('一', '二', '三', '四','五')
tup2 = (1, 2, 3, 4, 5 )

print ("tup1[0]: ", tup1[0]) 
print ("tup2[1:5]: ", tup2[1:5])

```

### 修改元组

元组中的元素值是不允许修改的，但我们可以对元组进行连接组合。

```
# 实例 2
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz') 
tup1[0] = 100 # 元组元素是不可修改的。
# 创建一个新的元组将两个元组组合
tup3 = tup1 + tup2 
print (tup3)
```

### 删除元组

元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组。

```python
# 实例 3
tup = ('一', '二', '三', '四','五')
print (tup)
del tup 
print ("删除后的元组 tup : ") 
print (tup)
```

以上实例元组被删除后，输出变量会有异常信息.

### 元组运算符

与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

![](.\images\Snipaste_2024-10-30_17-53-59.png)

### 元组索引，截取

因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素。

```python
# 实例 4
tup = ('一', '二', '三', '四','五')
print(tup[1])
print(tup[-1])
print(tup[1:-2])
```

### 元组内置函数

[Python元组](https://so.csdn.net/so/search?q=Python元组&spm=1001.2101.3001.7020)包含了以下内置函数

![](F:\培训\images\Snipaste_2024-10-30_17-54-51.png)

## 9.字典
字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号( , )分割，整个字典包括在花括号 {} 中 。

dict 作为 Python 的关键字和内置函数，变量名不建议命名为 dict。

键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字。


```
# 实例 1
tinydict = {'name': 'zhangsan', 'grade': 1, 'url': 'www.baidu.com'}
print(tinydict)
```

### 创建空字典

使用大括号 { } 创建空字典。

```
# 实例 2

# 使用大括号 {} 来创建空字典  
emptyDict = {}     
# 打印字典  
print(emptyDict)     
# 查看字典的数量  
print("Length:", len(emptyDict))     
# 查看类型  
print(type(emptyDict))

```

使用内建函数 dict() 创建字典。

```

# 实例 3
emptyDict = dict()   
# 打印字典  
print(emptyDict)    
# 查看字典的数量  
print("Length:",len(emptyDict))    
# 查看类型  
print(type(emptyDict))

```

访问字典里的值
把相应的键放入到方括号中。

```

# 实例 4
tinydict = {'Name': 'zhangsan', 'Age': 7, 'Class': 'First'}
print("tinydict['Name']: ", tinydict['Name'])
print("tinydict['Age']: ", tinydict['Age'])

```

如果用字典里没有的键访问数据，会输出错误。

```python
# 实例 5
tinydict = {'Name': 'zhangsan', 'Age': 7, 'Class': 'First'}
print("tinydict['Alice']: ", tinydict['Alice'])
```

### 修改字典

向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对

```
# 实例 6
tinydict = {'Name': 'zhangsan', 'Age': 7, 'Class': 'First'}
tinydict['Age'] = 8 # 更新 Age 
tinydict['School'] = "X大学" # 添加信息 
print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

```

可以出Age从7变成8，多添加了个键与值。

### 举一反三

创建一个空字典在里面添加水果和蔬菜这两个键，水果值为苹果、蔬菜值为西红柿，再把西红柿改成马铃薯。

```
# 练习 1
Dict = {}
Dict['fruit'] = "苹果" 
Dict['vegetables'] = "西红柿"  
print("Dict['fruit']: ", Dict['fruit'])
print("Dict['vegetables']: ", Dict['vegetables'])
Dict['vegetables'] = "马铃薯"
print("Dict['vegetables']: ", Dict['vegetables'])

```

### 删除字典元素

能删单一的元素也能清空字典`.clear()`，清空只需一项操作，显式删除一个键或字典用del命令典。

```
# 实例 7
tinydict = {'Name': 'zhangsan', 'Age': 7, 'Class': 'First'}
del tinydict['Name'] # 删除键 'Name' 
tinydict.clear() # 清空字典 
del tinydict # 删除字典
print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

```

字典键的特性
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：

不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住。
键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行。
字典内置函数与方法
Python字典包含了以下内置函数：

| 序号 | 函数及描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1    | len(dict) 计算字典元素个数，即键的总数。                     |
| 2    | str(dict) 输出字典，可以打印的字符串表示。                   |
| 3    | type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。 |

### Python字典包含了以下内置方法：

![](.\images\Snipaste_2024-10-30_18-00-50.png)

集合
集合（set）是一个无序的不重复元素序列。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

```
# 实例 1
# 可以理解为这个是一个没有键，只有值的字典，也叫做集合。
fruit = {'apple', 'orange', 'pear', 'orange', 'banana'}
print(fruit)

# set()集合函数
a = set('abcccd')
print(a)
b = set('ad')
c = a-b 
print(c)

```

可以看出输出结果不是固定的，是个无序的不重复元素序列。

1. a-b（集合a中包含而集合b中不包含的元素）
2. a|b（集合a或b中包含的所有元素）
3. a&b（集合a和b中都包含了的元素）
4. a^b（不同时包含于a和b的元素）

## 10.集合的基本操作

### 添加元素

1. add()函数，将元素添加到集合中，如果元素已存在，则不进行任何操作。
2. update()函数，添加元素，且参数可以是列表，元组，字典等。

```
# 实例 2
fruit = set(("apple", "orange", "pear"))
fruit.add("banana")
print(fruit)
fruit.update({1,2,3})
print(fruit)
```

### 移除元素

1. remove()函数，将元素从集合中移除，如果元素不存在，则会发生错误。
2. discard()函数，将元素从集合中移除，且如果元素不存在，不会发生错误。
3. pop()函数，将集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。

```
# 实例 3
fruit = set(("apple", "orange", "pear","banana"))
fruit.remove("apple")
print(fruit)
fruit.discard("banana")
print(fruit)
fruit.pop()
print(fruit)

```

### 计算集合元素个数

len()函数，计算集合元素个数。

```python
# 实例 4
fruit = set(("apple", "orange", "pear","banana"))
print(len(fruit))
```

### 清空集合

clear()函数，清空集合。

```python
# 实例 5
fruit = set(("apple", "orange", "pear","banana"))
fruit.clear()
print(fruit)
```

### 判断元素是否在集合中存在

in,判断元素是否在集合中，存在返回 True，不存在返回 False。

```
# 实例 5
fruit = set(("apple", "orange", "pear","banana"))
print("apple" in fruit)
print("peach" in fruit)
```

### 集合内置方法完整列表

![](.\images\Snipaste_2024-10-30_18-06-08.png)