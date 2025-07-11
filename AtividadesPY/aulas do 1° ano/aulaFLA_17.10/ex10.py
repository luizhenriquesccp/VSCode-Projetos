import turtle


    
t = turtle.Turtle()
    
    
t.penup()
t.goto(-100, 100)
t.pendown()
t.shape("turtle")  
    
t.color("red")  
for _ in range(4):
        t.forward(100)
        t.right(90)
    
    
t.penup()
t.goto(100, 100)
t.pendown()
t.shape("square")  
    
t.color("blue")  
for _ in range(4):
        t.forward(100)
        t.right(90)
    
    
t.penup()
t.goto(-100, -100)
t.pendown()
t.shape("classic")  
    
t.color("yellow")  
for _ in range(4):
        t.forward(100)
        t.right(90)
    
    
t.penup()
t.goto(100, -100)
t.pendown()
t.shape("triangle")  
    
t.color("green")  
for _ in range(4):
        t.forward(100)
        t.right(90)
        
t.penup()
t.goto(300,150)
t.pendown()

t.shape("arrow")
t.color("purple")

for _ in range(4):
	t.right(90)
	t.forward(430)

    
    
 