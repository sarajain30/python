
import turtle

al = turtle
al.shape("turtle")
al.color("black")
al.width(1100)
al.speed(0)

al.forward(1)

al.color("cyan")
al.width(3)
for i in range(50):
    al.circle(100, 300)
    al.left(290)


input()