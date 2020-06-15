def setup():
    size(500, 500)
    textSize(100)
    textAlign(CENTER)
    text("M", width/2-50, height/2)
    text("S", width/2+50, height/2)

def draw():
    clear()
    background(150, 50, 150)
    
    s = createShape()
    s.beginShape()
    s.fill(100, 0, 100)
    s.stroke(0)
    s.vertex(width/2-100, height/3*2)
    s.vertex(width/2-50, height/3*2+50)
    s.vertex(width/2, height/3*2)
    s.endShape(CLOSE)
    shape(s, 40, -65)
    
    if (mousePressed == True):
        text("M", width/2-50, height/2)
        fill(100, 20, 70)
        
    if keyPressed:
        if (keyCode == LEFT):
            fill(100, 20, 70)
            text("M", width/2-50, height/2)
            fill(150, 50, 150)
            text("S", width/2+50, height/2)
        if (keyCode == RIGHT):
            fill(255)
            text("S", width/2+50, height/2)
            fill(150, 50, 150)
            text("M", width/2-50, height/2)

    if keyPressed:
        fill(255)
        if key == 's' or key == 'S':
            text("S", width/2+50, height/2)

        
