class Person:
    # __init__ 方法会在类的对象被实例化（Instantiated）时立即运行
    # 就像java中的构造方法
    # 这一方法可以对任何你想进行操作的目标对象进行初始化（Initialization）操作
    # 初始化的时候传入两个参数
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("hello, my name is ", self.name)


Person("ran").say_hi()
# 也可以用下面这种写法
p = Person("ran")
p.say_hi()

