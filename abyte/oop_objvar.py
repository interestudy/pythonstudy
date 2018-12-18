class Robot:
    """表示有一个带有名字的机器人。"""

    # 一个变量 用来记录机器人的数量
    # 注意当一个对象变量与一个类变量名称相同时，类变量将会被隐藏
    population = 0

    def __init__(self, name):
        """初始化数据"""

        self.name = name
        print("Initializing... {}".format(self.name))

        # 有人创建时 机器人数量增加
        Robot.population += 1

    def die(self):
        """我挂了。"""
        print("{} is being destroyed".format(self.name))

        # 有人创建时 机器人数量增加
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} robots working".format(Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候

               没问题，你做得到。"""
        print("Greetings, my master call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """打印出当前机器人的数量"""
        print("We have {:d} robots.".format(cls.population))


robot1 = Robot("ran")
robot1.say_hi()
Robot.how_many()

robot2 = Robot("san")
robot2.say_hi()
robot2.how_many()

robot1.die()
robot2.die()

Robot.how_many()
# 打印文档
print(Robot.say_hi.__doc__)
