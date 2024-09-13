#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100  // 定义数组的最大长度

// 函数声明
void add(int arr[], int* size, int element);                               //增加子函数
void delete(int arr[], int* size, int element);                     //删除子函数
void modify(int arr[], int* size, int oldelement, int newelement);  //修改子函数
int find(int arr[], int size, int element);                         //查找子函数
void sort(int arr[], int size);                                       //排序子函数
void display(int arr[], int size);                                    //显示数组子函数

int main()
{
    int arr[MAX_SIZE] = { 0 };  // 初始化数组
    int size = 0;             // 当前数组中的元素个数
    int choice, element, num, newelement, oldelement;

    while (1)                //循环以实现不同功能
    {
        printf("\n请选择操作：\n");
        printf("1. 增加\n");
        printf("2. 删除\n");
        printf("3. 修改\n");
        printf("4. 查找\n");
        printf("5. 排序\n");
        printf("6. 退出\n");
        scanf_s("%d", &choice);     //输入功能序号

        switch (choice)
        {
        case 1:    //逐个增加数组中元素
            printf("请输入要增加的元素：");
            scanf_s("%d", &element);
            add(arr, &size, element);
            break;
        case 2:    //从前到后的顺序删除指定元素
            printf("请输入要删除的元素：");
            scanf_s("%d", &element);
            delete(arr, &size, element);
            break;
        case 3:    //修改元素
            printf("请输入要修改的元素：");
            scanf_s("%d", &oldelement);
            printf("请输入新值：");
            scanf_s("%d", &newelement);
            modify(arr, &size, oldelement, newelement);
            break;
        case 4:    //查找元素
            printf("请输入要查找的元素：");
            scanf_s("%d", &element);
            num = find(arr, size, element);
            if (num != -1)
            {
                printf("元素找到，位置：%d\n", num);  //显示所查找元素在数组中位置
            }
            else
            {
                printf("元素未找到\n");
            }
            break;
        case 5:    //从小到大对数组元素排序
            sort(arr, size);
            break;
        case 6:
            printf("退出程序。\n");
            exit(0);
        default:
            printf("无效的选择，请重新输入。\n");
        }

        // 显示当前数组状态
        printf("当前数组：");
        display(arr, size);
    }

    return 0;
}

// 实现各个子函数
void add(int arr[], int* size, int element)
{
    if (*size < MAX_SIZE)
    {
        arr[*size] = element;
        (*size)++;
    }    //通过指针int* size 实现地址传递从而改变size 更新数组状态
    else
    {
        printf("数组已满，无法添加新元素。\n");
    }
}

void delete(int arr[], int* size, int element)  //增加删除修改都会改变数组元素从而导致数组状态改变所以都使用指针
{
    int i, j;
    for (i = 0; i < *size; i++)
    {
        if (arr[i] == element)
        {
            for (j = i; j < *size - 1; j++)
            {
                arr[j] = arr[j + 1];
            }
            (*size)--;
            return;         //把要删除的元素过虑并保持过虑后数组顺序不变
        }
    }
    printf("元素未找到，无法删除。\n");
}

void modify(int arr[], int* size, int oldelement, int newelement)
{
    for (int i = 0; i < *size; i++)
    {
        if (arr[i] == oldelement)
        {
            arr[i] = newelement;
            return;
        }
    }                              //实现新旧元素的替换
    printf("元素未找到，无法修改。\n");
}

int find(int arr[], int size, int element)
{
    for (int i = 0; i < size; i++)   //遍历数组并返回所找元素的位置
    {
        if (arr[i] == element)
        {
            return i;
        }
    }
    return -1;  // 元素未找到
}

void sort(int arr[], int size)
{
    //从小到大排序
    int temp;
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = 0; j < size - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                // 交换元素
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void display(int arr[], int size)
{
    for (int i = 0; i < size; i++)   //从前到后输出数组中的各元素
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}



