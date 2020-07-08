def setup():

    global img
    size(1200/2, 1600/2)
    noFill()
    strokeWeight(10)

def draw():

    global img
    img = loadImage("sans.png")
    try:
        image(img, 50,100, 500,500)
            
    except:
        print ("Error!")
        stroke(255,0,0,100) 
    else:
        stroke(0,0,255,100)
    finally:
        rect(20, 75,555,555)
        
# 1,5pkt
