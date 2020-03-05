def setup():
    size(400,600)
    stroke(255)
    rectMode(CORNER)
def draw():
    print(mouseX,mouseY,mousePressed)
    rect(100,150,200,200)
    if mousePressed:
        rect(0,0,mouseX,mouseY)
