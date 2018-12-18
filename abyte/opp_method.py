class Person:
    def say_hi(self):
        print('Hello, how are you?')
        print(self)
        print(self.__class__)


p = Person()
p.say_hi()
# 前面两行同样可以写作
# Person().say_hi()
# 这里我们就能看见 self 是如何行动的了。要注意到 say_hi 这一方法不需要参数，但是依旧在函数定义中拥有 self 变量
