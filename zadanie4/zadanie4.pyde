add_library("pdf")

def setup():
    global img
    global i
    size(198, 255)
    beginRecord(PDF, "pdfzadanie.pdf")
    img=loadImage("zdjeciedowod.jpg")
    imageMode(CENTER)
    image(img, width/2, height/2)
    
def draw():
    global img
    global i
    if (mousePressed == True):
        i = loadImage("okulary.png")
        image(i, width/2, 135, 140, 70)
        endRecord()
        
#1,5pkt
