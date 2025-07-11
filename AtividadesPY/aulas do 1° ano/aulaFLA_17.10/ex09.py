import turtle

le = turtle.Turtle()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']  

for i in range(180):  

    le.color(colors[i % len(colors)])  
    
    le.forward(2)  
    
    le.right(2)  

