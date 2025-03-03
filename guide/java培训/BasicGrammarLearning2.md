# 注释
单行注释，多行注释，文档注释

```java
public class comment {
    public static void main(String[] args) {
    //我是单行注释
    System.out.println("Hello World");

        /*
        * 我是多行注释
        *
        * */

    }
}
```

# 变量
Java语言提供了八种基本类型。六种数字类型（四个整数型，两个浮点型），一种字符类型，还有一种布尔型。
byte：
byte 数据类型是8位、有符号的，以二进制补码表示的整数

short：
short 数据类型是 16 位、有符号的以二进制补码表示的整数

int：
int 数据类型是32位、有符号的以二进制补码表示的整数

long：
long 数据类型是 64 位、有符号的以二进制补码表示的整数

float：
float 数据类型是单精度、32位浮点数

double：
double 数据类型是双精度、64 位的浮点数
浮点数的默认类型为 double 类型

boolean：
只有两个取值：true 和 false

char：
char 类型是一个单一的 16 位 Unicode 字符

变量使用
```java
public class Variable {
    public static void main(String[] args) {
        //声明变量
        int var;
        //赋值
        var = 10;
        System.out.println(var);
        //也可以一步完成
        int var2 = 10;
    }
}
```
# 自动类型转换
整型、实型（常量）、字符型数据可以混合运算。运算中，不同类型的数据先转化为同一类型，然后进行运算
转换从低级到高级，byte,short,char—> int —> long—> float —> double 
注意：
不能对boolean类型进行类型转换。 在把容量大的类型转换为容量小的类型时必须使用强制类型转换。 转换过程中可能导致溢出或损失，
精度浮点数到整数的转换是通过舍弃小数得到，而不是四舍五入

```java
public class TypeConversion {
    public static void main(String[] args) {
        char x1='a';//定义一个char类型
        int y1 = x1;//char自动类型转换为int
        System.out.println("char自动类型转换为int后的值等于"+ y1);
        char x2 = 'A';//定义一个char类型
        int y2 = x2+1;//char 类型和 int 类型计算
        System.out.println("char类型和int计算后的值等于"+ y2);
        //浮点型转整形
        System.out.println((int)333.67);
    }
}
```
# String类
字符串广泛应用 在 Java 编程中，在 Java 中字符串属于对象，Java 提供了 String 类来创建和操作字符串。
```java
public class STRING {
    public static void main(String[] args) {
        String s = "Hello World";
        System.out.println(s);
        
    }
}

```


