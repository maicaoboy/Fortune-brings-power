import turtle as t

p = t.Turtle()
t.colormode(255)
t.bgcolor(196, 31, 38)
t.setup(1300, 700, 0, 0)
p.speed(0)


def waikuang():
    """画外框"""
    p.color(223, 186, 95)
    p.pensize(5)
    p.up()
    p.goto(-560, 300)
    p.down()
    """第一个中国结"""
    p.right(90)
    p.forward(60)
    p.right(90)
    p.forward(20)
    p.right(90)
    p.forward(60)
    p.left(90)
    p.forward(20)
    p.left(90)
    p.forward(20)
    p.left(90)
    p.forward(60)
    p.right(90)
    p.forward(20)
    p.right(90)
    p.forward(60)
    p.left(90)
    p.forward(520)
    """第二个中国结"""
    p.left(90)
    p.forward(60)
    p.right(90)
    p.forward(20)
    p.right(90)
    p.forward(60)
    p.left(90)
    p.forward(20)
    p.left(90)
    p.forward(20)
    p.left(90)
    p.forward(60)
    p.right(90)
    p.forward(20)
    p.right(90)
    p.forward(60)
    p.left(90)
    p.forward(1120)
    """第三个中国结"""
    p.left(90)
    p.forward(60)
    p.right(90)
    p.forward(20)
    p.right(90)
    p.forward(60)
    p.left(90)
    p.forward(20)
    p.left(90)
    p.forward(20)
    p.left(90)
    p.forward(60)
    p.right(90)
    p.forward(20)
    p.right(90)
    p.forward(60)
    p.left(90)
    p.forward(520)
    """第四个中国结"""
    p.left(90)
    p.forward(60)
    p.right(90)
    p.forward(20)
    p.right(90)
    p.forward(60)
    p.left(90)
    p.forward(20)
    p.left(90)
    p.forward(20)
    p.left(90)
    p.forward(60)
    p.right(90)
    p.forward(20)
    p.right(90)
    p.forward(60)
    p.left(90)
    p.forward(1120)

def number2022():
    p.up()
    p.goto(-450, 225)
    p.pensize(15)
    p.down()
    p.forward(50)
    p.right(90)
    p.forward(50)
    p.right(90)
    p.forward(100)
    p.right(90)
    p.forward(100)
    p.right(90)
    p.forward(100)
    p.left(90)
    p.forward(100)
    p.left(90)
    p.forward(100)
    p.left(90)
    p.forward(50)
    p.left(90)
    p.forward(50)
    p.right(180)
    p.forward(100)
    p.left(90)
    p.forward(50)
    p.right(90)
    p.forward(100)
    p.right(90)
    p.forward(200)
    p.right(90)
    p.forward(100)
    p.right(90)
    p.forward(100)

    p.up()
    p.goto(-450, -25)
    p.down()
    p.left(90)
    p.forward(50)
    p.right(90)
    p.forward(50)
    p.right(90)
    p.forward(100)
    p.right(90)
    p.forward(100)
    p.right(90)
    p.forward(100)
    p.left(90)
    p.forward(100)
    p.left(90)
    p.forward(100)
    p.left(90)
    p.forward(50)
    p.left(90)
    p.forward(50)
    p.backward(150)
    p.forward(50)
    p.right(90)
    p.forward(50)
    p.right(90)
    p.forward(100)
    p.right(90)
    p.forward(100)
    p.right(90)
    p.forward(100)
    p.left(90)
    p.forward(100)
    p.left(90)
    p.forward(100)
    p.left(90)
    p.forward(50)
    p.left(90)
    p.forward(50)



def tiger():
    """虎头主体金色"""
    p.pensize(8)
    p.up()
    p.home()
    p.goto(600, 200)
    p.down()
    p.left(180)
    p.begin_fill()
    p.fillcolor(223, 186, 95)
    p.forward(160)
    p.left(45)
    p.forward(160)
    p.left(20)
    p.forward(50)
    p.right(20)
    p.forward(100)
    p.left(45)
    p.forward(20)
    p.left(90)
    p.forward(50)
    p.right(90)
    p.forward(35)
    p.left(90)
    p.forward(160)
    p.right(45)
    p.forward(70)
    p.left(45)
    p.forward(70)
    p.right(45)
    p.forward(50)
    p.left(135)
    p.forward(400)
    p.end_fill()

    """嘴巴"""
    p.up()
    p.color('black')
    p.goto(278, -50)
    p.left(90)
    p.down()
    p.begin_fill()
    p.color('white')
    p.fillcolor('white')
    p.forward(74)
    p.left(135)
    p.forward(135)
    p.left(45)
    p.forward(98)
    p.right(135)
    p.forward(44)
    p.right(60)
    p.forward(62)
    p.left(150)
    p.forward(58)
    p.right(135)
    p.forward(30)
    p.left(90)
    p.forward(47)
    p.left(90)
    p.forward(67)
    p.left(45)
    p.forward(155)
    p.left(90)
    p.forward(70)
    p.left(45)
    p.forward(155)
    p.right(90)
    p.forward(40)
    p.left(90)
    p.forward(20)
    p.end_fill()
    """鼻子三角形"""
    p.up()
    p.home()
    p.goto(284, -46)
    p.pensize(2)
    p.left(180)
    p.begin_fill()
    p.color('black')
    p.fillcolor('black')
    p.forward(90)
    p.left(135)
    p.forward(54)
    p.left(90)
    p.forward(54)
    p.end_fill()
    """嘴巴毛"""
    p.up()
    p.goto(248, -100)
    p.right(45)
    p.down()
    p.pensize(7)
    p.forward(70)
    p.up()
    p.goto(264, -115)
    p.down()
    p.forward(70)
    """嘴巴黑色"""
    p.up()
    p.pensize(2)
    p.goto(282, -135)
    p.down()
    p.begin_fill()
    p.forward(120)
    p.right(45)
    p.forward(41)
    p.right(90)
    p.forward(90)
    p.right(90)
    p.forward(43)
    p.right(90)
    p.forward(70)
    p.left(135)
    p.forward(90)
    p.right(45)
    p.forward(21)
    p.end_fill()
    """尖牙旁边黑色的"""
    p.up()
    p.home()
    p.goto(335, -198)
    p.down()
    p.left(135)
    p.begin_fill()
    p.forward(30)
    p.left(135)
    p.forward(20)
    p.left(90)
    p.forward(40)
    p.end_fill()

    """耳朵部分"""
    """白色主体"""
    p.up()
    p.home()
    p.goto(460, 240)
    p.right(90)
    p.down()
    p.color('white')
    p.fillcolor('white')
    p.begin_fill()
    p.forward(120)
    p.right(45)
    p.forward(50)
    p.left(45)
    p.forward(15)
    p.right(45)
    p.forward(115)
    p.right(90)
    p.forward(10)
    p.right(90)
    p.forward(85)
    p.left(135)
    p.forward(60)
    p.right(90)
    p.forward(48)
    p.right(45)
    p.forward(145)
    p.left(45)
    p.forward(33)
    p.right(90)
    p.forward(21)
    p.right(90)
    p.forward(20)
    p.end_fill()
    """黑色部分"""
    p.backward(20)
    p.color('black')
    p.fillcolor('black')
    p.begin_fill()
    p.forward(120)
    p.left(90)
    p.forward(120)
    p.left(135)
    p.forward(175)
    p.end_fill()
    """1"""
    p.up()
    p.home()
    p.goto(460, 118)
    p.down()
    p.begin_fill()
    p.right(90)
    p.forward(15)
    p.right(45)
    p.forward(50)
    p.right(135)
    p.forward(15)
    p.right(45)
    p.forward(50)
    p.end_fill()

    """2"""
    p.up()
    p.goto(334, 56)
    p.right(45)
    p.down()
    p.begin_fill()
    p.forward(60)
    p.right(135)
    p.forward(85)
    p.right(90)
    p.forward(15)
    p.right(90)
    p.forward(15)
    p.left(45)
    p.forward(40)
    p.end_fill()

    """3"""
    p.up()
    p.home()
    p.goto(362, 5)
    p.down()
    p.begin_fill()
    p.right(90)
    p.forward(30)
    p.right(45)
    p.forward(30)
    p.left(45)
    p.forward(17)
    p.left(135)
    p.forward(50)
    p.left(45)
    p.forward(48)
    p.end_fill()

    """4 眼睛"""
    p.up()
    p.home()
    p.goto(375, 65)
    p.down()
    p.begin_fill()
    p.forward(20)
    p.left(90)
    p.forward(28)
    p.left(90)
    p.forward(20)
    p.left(90)
    p.forward(28)
    p.end_fill()

    """5 6 王"""
    p.up()
    p.home()
    p.goto(335, 105)
    p.down()
    p.begin_fill()
    p.forward(50)
    p.left(45)
    p.forward(20)
    p.left(135)
    p.forward(50)
    p.end_fill()

    p.up()
    p.home()
    p.goto(375, 145)
    p.down()
    p.begin_fill()
    p.forward(40)
    p.left(45)
    p.forward(20)
    p.left(135)
    p.forward(40)
    p.end_fill()

    """7"""
    p.up()
    p.home()
    p.goto(325, -60)
    p.down()
    p.begin_fill()
    p.right(90)
    p.forward(13)
    p.left(45)
    p.forward(16)
    p.left(45)
    p.forward(40)
    p.left(45)
    p.forward(60)
    p.right(45)
    p.forward(55)
    p.right(45)
    p.forward(15)
    p.right(45)
    p.forward(70)
    p.left(45)
    p.forward(20)
    p.left(135)
    p.forward(100)
    p.left(45)
    p.forward(15)
    p.right(45)
    p.forward(60)
    p.right(45)
    p.forward(15)
    p.left(45)
    p.forward(30)
    p.left(135)
    p.forward(50)
    p.left(45)
    p.forward(60)
    p.right(90)
    p.forward(40)
    p.left(45)
    p.forward(75)
    p.right(45)
    p.forward(30)
    p.right(45)
    p.forward(24)
    p.end_fill()

    """8"""
    p.up()
    p.home()
    p.goto(497, 95)
    p.down()
    p.begin_fill()
    p.right(90)
    p.forward(22)
    p.left(45)
    p.forward(50)
    p.right(45)
    p.forward(90)
    p.left(45)
    p.forward(60)
    p.right(45)
    p.forward(50)
    p.right(135)
    p.forward(30)
    p.right(45)
    p.forward(170)
    p.left(45)
    p.forward(81)
    p.end_fill()

    """9"""
    # # p.up()
    # p.home()
    # p.goto(588, 205)
    # p.down()
    # p.begin_fill()

def lantern():
    p.up()
    p.home()
    p.right(90)
    p.goto(-150, 297)
    p.down()
    p.color(223, 186, 95)
    p.pensize(10)
    p.forward(80)
    p.begin_fill()
    p.fillcolor(223, 186, 95)
    p.left(90)
    p.circle(-40)
    p.right(90)
    p.up()
    p.forward(80)
    p.down()
    p.left(90)
    p.circle(-40)
    p.right(90)
    p.up()
    p.forward(80)
    p.down()
    p.left(90)
    p.circle(-40)
    p.right(90)
    p.up()
    p.forward(80)
    p.down()
    p.left(90)
    p.circle(-40)
    p.right(90)
    p.end_fill()

    p.up()
    p.forward(83)
    p.down()
    p.begin_fill()
    p.pensize(1)
    p.left(90)
    p.forward(10)
    p.right(90)
    p.forward(10)
    p.right(90)
    p.forward(20)
    p.right(90)
    p.forward(100)
    p.right(90)
    p.forward(10)
    p.end_fill()
    p.right(90)
    p.pensize(4)
    p.forward(135)
    p.pensize(1)
    p.left(90)
    p.begin_fill()
    p.forward(7)
    p.right(90)
    p.forward(14)
    p.right(90)
    p.forward(14)
    p.right(90)
    p.forward(14)
    p.right(90)
    p.forward(7)
    p.end_fill()
    p.right(90)
    p.forward(14)
    p.right(90)
    p.forward(6)
    p.left(90)
    for i in range(7):
        p.forward(90)
        p.backward(90)
        p.left(90)
        p.forward(2)
        p.right(90)


def tigeryin():
    p.up()
    p.home()
    p.right(90)
    p.goto(0, -120)
    p.down()
    p.left(135)
    p.begin_fill()
    p.circle(-80, steps=4)
    p.end_fill()

    p.left(45)
    p.pensize(7)
    p.up()
    p.goto(-13.5, -177)
    p.down()
    p.dot(10)
    p.color(196, 31, 38)
    p.circle(-70)
    p.goto(-20, -177)
    p.pensize(10)
    p.circle(-76)
    p.right(90)
    p.forward(10)
    p.up()
    p.forward(10)
    p.right(90)
    p.forward(50)
    p.down()
    p.write('虎', font=("方正舒体", 80, "bold"))
    p.up()
    p.forward(33)
    p.left(90)
    p.forward(25)
    p.down()
    p.color(233, 186, 95)
    p.write('壬寅年', font=("方正姚体", 15, "bold"))

def wenzi():
    p.up()
    p.home()
    p.goto(-190, 137)
    p.down()
    p.color(196, 31, 38)
    p.write('新', False, font=("STXinwei", 60, "bold"))
    for word in '年快乐':
        p.up()
        p.right(90)
        p.forward(80)
        p.left(90)
        p.write(word, False, font=("STXinwei", 60, "bold"))

def wenzi1():
    p.up()
    p.home()
    # p.goto(-50, 150)
    p.goto(-50, 65)
    p.down()
    p.color(223, 186, 95)
    p.write('福', False, font=("STXinwei", 80, "bold"))
    p.up()
    p.forward(100)
    p.down()
    p.write('虎', False, font=("STXinwei", 80, "bold"))
    p.up()
    p.backward(100)
    p.right(90)
    p.forward(100)
    p.left(90)
    p.down()
    p.write('生', False, font=("STXinwei", 80, "bold"))
    p.up()
    p.forward(100)
    p.down()
    p.write('威', False, font=("STXinwei", 80, "bold"))

def shanzi(x, y, size):
    p.up()
    p.home()
    p.pensize(4)
    p.goto(x, y)
    p.down()
    p.color(223, 186, 95)
    p.right(30)
    p.backward(size)
    p.forward(size)
    p.left(30)
    p.forward(size / 2)
    p.left(30)
    p.forward(size)
    p.left(90)
    p.circle(size + pow(3, 1/2) * 2 / 3 * size / 4, 120)
    p.left(90)
    p.forward(size / 4)
    p.left(90)
    p.circle(-(size * 3 / 4 + pow(3, 1/2) * 2 / 3 * size / 4), 120)
    p.right(90)
    p.forward(size / 4)
    p.right(90)
    p.circle(size * 2 / 4 + pow(3, 1/2) * 2 / 3 * size / 4, 120)
    p.left(90)
    p.forward(size / 4)
    p.left(90)
    p.circle(-(size * 1 / 4 + pow(3, 1/2) * 2 / 3 * size / 4), 120)
    p.right(90)
    p.forward(size / 4)
    p.right(90)
    p.circle(pow(3, 1/2) * 2 / 3 * size / 4, 120)


def baozhu(x=250, y=298, length=50):
    p.up()
    p.home()
    p.pensize(5)
    p.goto(x, y)
    p.down()
    p.color(223, 186, 95)
    p.pensize(3)
    p.right(90)
    p.forward(length)
    p.left(45)
    p.begin_fill()
    for  i in range(4):
        p.forward(30)
        p.right(90)
    p.end_fill()
    for  i in range(2):
        p.forward(30)
        p.right(90)
    p.left(135)
    p.forward(5)
    for i in range(4):
        p.pensize(3)
        p.forward(10)
        p.left(45)
        p.pensize(10)
        p.forward(20)
        p.backward(20)
        p.right(45)
        p.pensize(3)
        p.forward(10)
        p.right(45)
        p.pensize(10)
        p.forward(20)
        p.backward(20)
        p.left(45)




"""中式角花外框"""
waikuang()

"""2022"""
number2022()

"""老虎"""
tiger()


"""灯笼"""
lantern()

"""虎印"""
tigeryin()


"""文字"""
"""新年快乐"""
wenzi()
"""福虎生威"""
wenzi1()


# """祥云彩纹"""
shanzi(-450, -270, 50)
shanzi(435, -150, 25)

"""爆竹"""
baozhu()
baozhu(-570, 240)
baozhu(-300, 170, 10)


print(pow(3, 1/2))

t.done()