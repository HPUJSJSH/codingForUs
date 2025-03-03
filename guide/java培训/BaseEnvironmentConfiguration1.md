# Java
# 基础介绍  
# 免责声明  
本JAVA教程仅适用于部门内部交流学习，请勿外传，另外此教程仅适用于新手入门，了解JAVA代码，能看懂基础的JAVA代码
，如果需要后续的深入学习，可以上网寻找或找学长询问
如遇到文档中未出现的问题请上网寻找解决办法。

# JDK介绍  
JDK为Java的开发工具包，已经包含JRE和Java开发工具

# JRE介绍  
JRE为Java运行环境，包含JVM（Java Virtual Machine）和Java的核心类库，下载JRE即可运行Java程序

# 配置环境变量（windows）
下载，安装JDK,在官网选择合适的JDK版本，下载到本地，请记好下载的路径。  

在我的电脑-属性-高级系统设置-环境变量  

中添加JAVA_HOME值为%  %\bin  
%中为JDK下载在本地的路径
验证在命令行中输入javac如果看到javac的参数信息即成功

# 开发工具
可以使用IDEA，vscode等软件
IDEA有社区版和专业版，社区版免费，已经能满足入门学习，专业版可免费使用一个月，但可使用学生账户免费使用
VSCODE需要配置相应插件


# 代码介绍
Java程序的文件命名与主类名相同以下面的代码为例，程序文件的名字为comment.java
public static void main(String[] args) {  }程序执行的入口，类似于C语言的main函数
{}里面写代码
```java
public class comment {
    public static void main(String[] args) {
        //System.out.println()调用输出方法输出（）中的内容
        System.out.println("Hello World");


    }
}
```


