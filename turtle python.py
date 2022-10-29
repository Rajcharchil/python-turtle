



#* Python program to draw square
# *using Turtle Programming

import turtle
crr = turtle.Turtle()
turtle.speed(12)
turtle.circle(50)
turtle.circle(20)

for i in range(70):
	crr.forward(30)
	crr.right(60)
crr.left(20)
    
turtle.done()







#Python program to draw
 #Spiral Helix Pattern
 #using Turtle Programming

import turtle
loadWindow = turtle.Screen()
turtle.speed(20)

for i in range(100):
	turtle.circle(1*i)
    
	turtle.circle(-1*i)
    
	turtle.left(i)

turtle.exitonclick()






  # Python program to draw
  # Rainbow Benzene
  # using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')


for x in range(360):
  
    t.pencolor(colors[x%6])
    t.width(x//200 + 1)
    t.forward(x)
    t.left(80)





# Python program to draw star
# using Turtle Programming
import turtle
star = turtle.Turtle()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('red')

star.right(75)
star.forward(100)

for i in range(32):
	star.right(140)
	star.forward(100)
	
turtle.done()




for i in range (100):
    if i % 2:
        continue
    print(i)
    
from itertools import count


num=int(input("enter a number greater than 1:"))

count=0
i=1
while i<=num:
    if num % i == 0:
        count=count+1
    i=i+1
    
if count==2:
    print("it is a prime number")
else:
    print("it is not a prime number")    



l1 = ["Hum","taa","auasj","easd"]
for name in l1:
    if name.startswitch("t"):
     print(name)



