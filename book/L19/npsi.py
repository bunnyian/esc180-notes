import turtle
import math

def draw_n():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90+55)
    turtle.forward(100/math.sin(55*(2*math.pi)/360))
    turtle.left(90+55)
    turtle.forward(100)
    
    #clean up
    turtle.penup()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90) 
    turtle.forward(10)
    turtle.pendown()
    
def draw_psi():
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    
    turtle.pendown()
    turtle.left(180)
    
    turtle.forward(20)
    turtle.left(30)
    turtle.forward(20)
    turtle.left(30)
    turtle.forward(20)
    turtle.left(30)
    turtle.forward(20)
    turtle.left(30)
    turtle.forward(20)
    turtle.left(30)
    turtle.forward(20)
    turtle.left(30)
    turtle.forward(20)
    
    turtle.penup()
    turtle.left(90)
    turtle.forward(0.5*20*(math.sin(0   * math.pi/180) +
                           math.sin(30  * math.pi/180) +
                           math.sin(60  * math.pi/180) +
                           math.sin(90  * math.pi/180) +
                           math.sin(120 * math.pi/180) +
                           math.sin(150 * math.pi/180) +
                           math.sin(180 * math.pi/180))   
                  )
    
    turtle.left(90)
    turtle.pendown()
    turtle.forward(100)
    
    turtle.penup()
    turtle.left(90)
    turtle.forward(0.5*20*(math.sin(0   * math.pi/180) +
                           math.sin(30  * math.pi/180) +
                           math.sin(60  * math.pi/180) +
                           math.sin(90  * math.pi/180) +
                           math.sin(120 * math.pi/180) +
                           math.sin(150 * math.pi/180) +
                           math.sin(180 * math.pi/180))   
                  )
    
   
    turtle.forward(10)
    
turtle.speed(1)
turtle.left(180)
turtle.penup()
turtle.forward(200)
turtle.left(180)
turtle.pendown()

draw_n()
draw_psi()

