# 面向对象
Java 作为一种面向对象的编程语言，  
类：类是一个模板，它描述一类对象的行为和状态。 例如动物。

对象：对象是类的一个实例，有状态和行为。例如，一条狗是一个对象是动物类的一个具体实例，
它的状态有：颜色、名字、品种；行为有：摇尾巴、叫、吃等。

# 定义类
语法格式  

修饰符 class 类名{}  
```
Java中，可以使用访问控制符来保护对类、变量、方法和构造方法的访问。Java 支持 4 种不同的访问权限。

default (即默认，什么也不写）: 在同一包内可见，不使用任何修饰符。使用对象：类、接口、变量、方法。

private : 在同一类内可见。使用对象：变量、方法。 注意：不能修饰类（外部类）

public : 对所有类可见。使用对象：类、接口、变量、方法

protected : 对同一包内的类和所有子类可见。使用对象：变量、方法。 注意：不能修饰类（外部类）。
```

# 创建对象
对象是根据类创建的。在Java中，使用关键字 new 来创建一个新的对象。创建对象需要以下三步：

声明：声明一个对象，包括对象名称和对象类型。
实例化：使用关键字 new 来创建一个对象。
初始化：使用 new 创建对象时，会调用构造方法初始化对象。

```java

public class Animal {
    //定义一个属性年龄为10
    public int age = 10;
    //定义一个方法获取输出年龄
    public int getAge() {
        return age;
    }

    //主方法
    public static void main(String[] args) {
        //动物类实例为小狗对象
        Animal dog = new Animal();
        //调用方法
        System.out.println(dog.getAge());
    }
}
```

# 属性/成员变量
属性是类的一个组成部分，一般是基本数据类型，也可以是引用类型
# 成员方法/方法
可以简单的理解为类内的方法，具体的调用机制自己下去了解

# 方法重载  
同一个类中可以有多个同名的方法，但参数不同。

```java 

public class Animal {
    
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }

    
    
}
```
# 构造器
在 Java 中，构造方法是用于创建类的对象的特殊方法。
当使用 new 关键字创建对象时，构造方法会自动调用，用来初始化对象的属性。
```
与类名相同：构造方法的名称必须与类名完全一致，包括大小写。这是构造方法的一个基本要求。

没有返回类型：构造方法没有返回类型声明，即使是 void 也不写。这使得它与普通方法区分开来。

自动调用：每次使用 new 创建对象时，构造方法会自动调用，以初始化对象的属性和状态。

不能直接调用：构造方法只能通过 new 关键字在创建对象时调用，不能像普通方法那样直接调用。


```
# this关键字

引用当前对象的属性或方法：当构造方法的参数名与类属性名相同时，使用 this 来区分类属性和参数。

```java
public class Person {
    //定义属性
    String name;
    int age;
    //构造方法
    public Person(String name, int age) {
        this.name = name;//this.name为Person这个类的name属性，name为实例化时传入的参数
        this.age = age;
    }


    public static void main(String[] args) {
        //利用构造器完成初始化
        Person person = new Person("John", 25);
    }
}

```