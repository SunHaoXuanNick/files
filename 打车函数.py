import  turtle as tu
def hanshu(a,b,c):
    tu.tracer(False)
    tu.showturtle()
    tu.hideturtle()
    tu.penup()
    tu.goto(-350,-175)
    tu.pensize(10)
    tu.pendown()
    tu.dot(20,"red")
    tu.goto(350,-175)
    tu.goto(335,-160)
    tu.goto(350,-175)
    tu.goto(335,-190)
    tu.penup()
    tu.goto(350,-200)
    tu.write("路程")
    tu.goto(-350,-175)
    tu.pendown()
    tu.goto(-350,175)
    tu.goto(-360,160)
    tu.goto(-350,175)
    tu.goto(-340,160)
    tu.penup()
    tu.goto(-360,190)
    tu.write('价格')
    tu.penup()
    #直角坐标系完成
    bei=20
    tu.pensize(5)
    #huizhihanshu
    chushi=-175+bei*a
    tu.goto(-350,chushi)
    tu.pendown()
    changdu=b*bei-350
    tu.goto(changdu,chushi)
    tu.dot(20,"red")
    tu.penup()
    #第一阶段绘制完成
    d=700/bei
    e=d-b
    f=c*e
    g=chushi+f
    tu.pendown()
    tu.goto(350,g)
    tu.penup()
    tu.goto(changdu,chushi)
    tu.dot(20,"red")
    tu.goto(-350,-175)
    tu.pensize(10)
    tu.pendown()
    tu.dot(20,"red")
    tu.done()
far=float(input("请输入第一阶段里程数（单位：千米）"))
price1=float(input("第一阶段价格价格（单位：元）"))
price2=float(input("第二阶段价格价格（单位：元/千米）"))
hanshu(price1,far,price2)