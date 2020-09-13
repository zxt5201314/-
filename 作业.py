from turtle import*
speed(200)
bgcolor("black")
sides = 6
colors =["red","yellow","blue","green","orange","purple"]
for i in range(125):
        pencolor(colors[i%sides])
        fd(i*3/sides+i)
        left(360/sides+1)
        width(i*sides/70)
        fd(i)
