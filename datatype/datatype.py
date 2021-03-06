"""
int  bool float complex string list

列表
元组
字典
字符串 在 Python 中可以使用 一对双引号 " 或者 一对单引号 ' 定义一个字符串

元组和列表之间的转换
使用 list 函数可以把元组转换成列表
list(元组)
使用 tuple 函数可以把列表转换成元组
tuple(列表)

不能以数字开头
不能与关键字重名
if :

elif:

else:

运算符
    //	取整除	返回除法的整数部分
    //=	取整除赋值运算符
    **	幂	又称次方、乘方，
    **=	幂赋值运算符
    and	 or  not

    成员运算符
    in
    not in

    运算符的优先级
    运算符	描述
    **	幂 (最高优先级)
    * / % //	乘、除、取余数、取整除
    + -	加法、减法
    <= < > >=	比较运算符
    == !=	等于运算符
    = %= /= //= -= += *= **=	赋值运算符
    in not in	成员运算符
    not or and	逻辑运算符

    循环
    while 条件(判断 计数器 是否达到 目标次数):
    for name in name_list:

     函数的文档注释
    在开发中，如果希望给函数添加注释，应该在 定义函数 的下方，使用 连续的三对引号
    在 连续的三对引号 之间编写对函数的说明文字
    在 函数调用 位置，使用快捷键 CTRL + Q 可以查看函数的说明信息


   Python 中数据类型可以分为 数字型 和 非数字型
    数字型
    整型 (int)
    浮点型（float）
    布尔型（bool）
    真 True 非 0 数 —— 非零即真
    假 False 0
    复数型 (complex)
    主要用于科学计算，例如：平面场问题、波动问题、电感电容等问题
    非数字型

    字符串
    列表
    元组
    字典
    在 Python 中，所有 非数字型变量 都支持以下特点：

    都是一个 序列 sequence，也可以理解为 容器
    取值 []
    遍历 for in
    计算长度、最大/最小值、比较、删除
    链接 + 和 重复 *
    切片



    变量的引用
    变量 和 数据 都是保存在 内存 中的
    在 Python 中 函数 的 参数传递 以及 返回值 都是靠 引用 传递的
        变量 和 数据 是分开存储的
        数据 保存在内存中的一个位置
        变量 中保存着数据在内存中的地址
        变量 中 记录数据的地址，就叫做 引用
        使用 id() 函数可以查看变量中保存数据所在的 内存地址


    可变和不可变类型
        不可变类型，内存中的数据不允许被修改：
        数字类型 int, bool, float, complex, long(2.x)
        字符串 str
        元组 tuple

        可变类型，内存中的数据可以被修改：
        列表 list
        字典 dict
    字典的 key 只能使用不可变类型的数据

    哈希 (hash)
        Python 中内置有一个名字叫做 hash(o) 的函数
        接收一个 不可变类型 的数据作为 参数
        返回 结果是一个 整数
        哈希 是一种 算法，其作用就是提取数据的 特征码（指纹）
        相同的内容 得到 相同的结果
        不同的内容 得到 不同的结果
        在 Python 中，设置字典的 键值对 时，会首先对 key 进行 hash 已决定如何在内存中保存字典的数据，以方便 后续 对字典的操作：增、删、改、查
        键值对的 key 必须是不可变类型数据
        键值对的 value 可以是任意类型的数据


    局部变量 是在 函数内部 定义的变量，只能在函数内部使用
    全局变量 是在 函数外部定义 的变量（没有定义在某一个函数内），所有函数 内部 都可以使用这个变量

        函数执行时，需要处理变量时 会：
            首先 查找 函数内部 是否存在 指定名称 的局部变量，如果有，直接使用
            如果没有，查找 函数外部 是否存在 指定名称 的全局变量，如果有，直接使用
            如果还没有，程序报错！

    函数不能直接修改 全局变量的引用
        在函数内部，可以 通过全局变量的引用获取对应的数据
        但是，不允许直接修改全局变量的引用 —— 使用赋值语句修改全局变量的值

        如果在函数中需要修改全局变量，需要使用 global 进行声明

    一个函数执行后能否返回多个结果
     在 Python 中，可以 将一个元组 使用 赋值语句 同时赋值给 多个变量
    注意：变量的数量需要和元组中的元素数量保持一致

    函数的参数
        不可变和可变的参数
        无论传递的参数是 可变 还是 不可变
        只要 针对参数 使用 赋值语句，会在 函数内部 修改 局部变量的引用，不会影响到 外部变量的引用

        如果传递的参数是 可变类型，在函数内部，使用 方法 修改了数据的内容，同样会影响到外部的数据

    多值参数
        有时可能需要 一个函数 能够处理的参数 个数 是不确定的，这个时候，就可以使用 多值参数
        python 中有 两种 多值参数：
        参数名前增加 一个 * 可以接收 元组
        参数名前增加 两个 * 可以接收 字典

        一般在给多值参数命名时，习惯使用以下两个名字
        *args —— 存放 元组 参数，前面有一个 *
        **kwargs —— 存放 字典 参数，前面有两个 *


    元组和字典的拆包
        在调用带有多值参数的函数时，如果希望：
        将一个 元组变量，直接传递给 args
        将一个 字典变量，直接传递给 kwargs
        就可以使用 拆包，简化参数的传递，拆包 的方式是：
        在 元组变量前，增加 一个 *
        在 字典变量前，增加 两个 *

"""


def add_data(data):
    result = 0
    while data > 0:
        result += data
        data -= 1
    return result


def mul_data(data):
    if data > 1:
        return data * mul_data(data -1);
    else:
        return 1


def int_data(data, is_right=True):
    result = 0
    if is_right:
        result = add_data(data)
    else:
        result = mul_data(data)
    return result


# 列表：（数组）
def list_operator():
    return 0

"""
元祖：-----------------与列表类似 不同之处为元祖的元素不能修改
表示多个元素组成的序列 
元祖用（）定义
"""

"""
字典用 {}定义
字典使用 键值对存储数据 用 ,逗号分隔  key 是索引 value是数据 键值必须唯一
"""

# 循环嵌套演练 —— 九九乘法表
