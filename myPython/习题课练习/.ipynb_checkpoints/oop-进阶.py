import random as r


class Turtle(object):

    def __init__(self):
        self.power = 100  # 初始化乌龟体力

        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)  # 初始化乌龟位置

    def move(self):
        new_x = r.choice([1, 2, -1, -2]) + self.x
        new_y = r.choice([1, 2, -1, -2]) + self.y

        # 接下来判断，乌龟的移动是否超出了边界
        if new_x < 0:
            new_x = 0 - (0 - new_x)
        elif new_x > 10:
            new_x = 10 - (10 - new_x)
        else:
            self.x = new_x

        if new_y < 0:
            new_y = 0 - (0 - new_y)
        elif new_y > 10:
            new_y = 10 - (10 - new_y)
        else:
            self.y = new_y

        self.power -= 1
        return (self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100


class Fish(object):

    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)  # 初始化鱼的位置

    def move(self):
        new_x = r.choice([1, -1, ]) + self.x
        new_y = r.choice([1, -1, ]) + self.y

        # 接下来判断，鱼的移动是否超出了边界
        if new_x < 0:
            new_x = 0 - (0 - new_x)
        elif new_x > 10:
            new_x = 10 - (10 - new_x)
        else:
            self.x = new_x

        if new_y < 0:
            new_y = 0 - (0 - new_y)
        elif new_y > 10:
            new_y = 10 - (10 - new_y)
        else:
            self.y = new_y

        return (self.x, self.y)


turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼被吃完了，游戏结束")
        break

    if not turtle.power:
        print("乌龟体力用完了，游戏结束")
        break

    pos = turtle.move()

        # 在迭代中对列表中的元素进行删除操作很危险，经常会出现一些意想不到的问题，因为迭代器是直接引用列表元素的数据的操作
        # 所以为了避免这种错误出现，我们把列表拷贝一份，然后对原列表进行操作

    for each_fish in fish[:]:
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼被吃掉了")