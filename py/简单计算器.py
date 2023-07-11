def calculator():
    print("欢迎使用简单计算器！")
    num1 = float(input("请输入第一个数字："))
    operator = input("请输入运算符（+、-、*、/）：")
    num2 = float(input("请输入第二个数字："))

    result = None
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("错误：除数不能为零！")

    if result is not None:
        print("计算结果：", result)

calculator()
```
编写一个简单的命令行计算器程序，可以进行加、减、乘、除四则运算。
```
