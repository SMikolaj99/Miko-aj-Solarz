def setup():
    size(600,600)
    frameRate(50)
    stroke(150,0,150)
    strokeWeight(2)
    global x, y
    x = 300
    y = 25

def draw():
    global x, y
    ellipse(x, y, 40, 40)
    x = x + 1
    y = y + 1
    if x > 575:
        x = x - 1
    if y > 575:
        y = y - 1
    if x < 25:
        x = x + 1
    if y < 25:
        y = y + 1
# wiem, że ponieważ polecenie if x > 575 przypisuje x podane wartości tylko wtedy
# kiedy spełnia warunek, koło nie może zmienić kierunku na stałe, jednak nie wiem
# jak temu zaradzić
        
