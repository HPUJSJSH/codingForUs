# 数组
Java 数组的声明、创建和初始化
# 声明数组变量

```
dataType[] arrayname;   // 首选的方法
 
dataType arrayname[];  // 效果相同，但不是首选方法
```
# 创建数组
Java语言使用new操作符来创建数组

```
//3种方式创建数组
arrayname = new dataType[arraySize];
dataType[] arrayname = new dataType[arraySize];
dataType[] arrayname= {value0, value1, ..., valuek};
```
```java
public class ArrayList {
    public static void main(String[] args) {
        //声明数组
        int arr1[];
        char arr2[];
        //创建数组
        arr1 = new int[10];
        //循环为数组赋值，并输出数组的值
        for (int i = 0; i < arr1.length; i++) {
            //利用索引访问数组元素，从0开始
            arr1[i] = i;
            System.out.print(arr1[i] + " ");
        }
    }
}

```
# 多维数组
多维数组可以看成是数组的数组,num1为行数，num2 为列数
```
dataType[][] arrayname = new dataType[num1][num2];

```