import random

def guess_number():
    target_number = random.randint(1, 100)
    while True:
        guess = int(input("请输入你猜的数字（1-100）："))
        if guess < target_number:
            print("猜小了！")
        elif guess > target_number:
            print("猜大了！")
        else:
            print("恭喜你，猜对了！")
            break

guess_number()
```
编写一个程序，让用户猜一个随机生成的数字，直到猜中为止。
```
