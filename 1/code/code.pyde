def setup():
    size(400,600)
    stroke(255)
    rectMode(CORNER)
def draw():
    print(mouseX,mouseY,mousePressed)
    rect(100,150,width/2,width/2) # tam gdzie sięda warto stosować zmienne zależne
    if mousePressed:
        rect(0,0,mouseX,mouseY)
    # w przeciwnym razie też miało się coś zadziać

# 1,5pkt
