import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(5)
t.color("#1F4E79")  

t.penup()
t.goto(-50, -100)
t.pendown()
t.goto(0, 100)
t.goto(50, -100)
t.penup()
t.goto(-25, 0)
t.pendown()
t.goto(25, 0)

t.penup()
t.goto(0, -160)
t.color("black")
t.write("Amity University", align="center", font=("Arial", 24, "bold"))

# Завершение
t.hideturtle()
turtle.done()
