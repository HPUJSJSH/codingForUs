# Java 循环结构  for, while 及 do...while
while 循环

while是最基本的循环，它的结构为：
```
while( 布尔表达式 ) {
//循环内容
}
```
只要布尔表达式为 true，循环就会一直执行下去。

do…while 循环
对于 while 语句而言，如果不满足条件，则不能进入循环。但有时候我们需要即使不满足条件，也至少执行一次。

do…while 循环和 while 循环相似，不同的是，do…while 循环至少会执行一次。
```
do {
//代码语句
}while(布尔表达式);
```
for循环
for 循环，使一些循环结构变得更加简单。 for循环执行的次数是在执行前就确定的。
```
for(初始化; 布尔表达式; 条件) {
    //代码语句
}
```
```java
public class Circulation {
    public static void main(String[] args) {
        //do-while演示
        int num1 = 2;
        
        do {
            System.out.println(num1);
            num1--;
        } while (num1 > 1);


        //for 演示
        for (int i = 0; i < 5; i++) {
            System.out.print(i);

        }
    }
}
```

# Java 条件语句 - if...else
Java 中的条件语句允许程序根据条件的不同执行不同的代码块。
一个 if 语句包含一个布尔表达式和一条或多条语句。

```
if(布尔表达式)
{
   //如果布尔表达式为true将执行的语句
}else{
   //如果布尔表达式的值为false
}

```

# if...else if...else 语句
```
if(布尔表达式 1){
   //如果布尔表达式 1的值为true执行代码
}else if(布尔表达式 2){
   //如果布尔表达式 2的值为true执行代码
}else if(布尔表达式 3){
   //如果布尔表达式 3的值为true执行代码
}else {
   //如果以上布尔表达式都不为true执行代码
}

```

```java
public class StructureDemo {
    public static void main(String[] args) {
        int num = 44;
        //if...else if...else 语句
        if (num < 10) {
            System.out.println(num);
        }
        else if(num > 50) {
            System.out.println(num);
        }
        else{
            System.out.println(num);
        }

    }
}

```
# break 关键字
break 主要用在循环语句或者 switch 语句中，用来跳出 整个 语句块。
# continue 关键字
continue 适用于任何循环控制结构中。作用是让程序立刻跳转到 下一次循环 的迭代。

# Java switch case 语句
switch case 语句判断一个变量与一系列值中某个值是否相等，每个值称为一个分支。
```
switch(expression){
    case value :
       //语句
       break; //可选
    case value :
       //语句
       break; //可选
    //你可以有任意数量的case语句
    default : //可选
       //语句
}
```
```java
public class StructureDemo {
    public static void main(String[] args) {
        int num = 44;
        //switch 演示
        switch (num){
            case 1:
                System.out.println("1");
            case 44:
                System.out.println("44");
                break;
                
            default:
                break;
        }

    }
}
```


































