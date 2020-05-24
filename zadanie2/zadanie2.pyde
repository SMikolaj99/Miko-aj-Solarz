def setup():
    size(600,600)
    frameRate(50)
    stroke(150,0,150)
    strokeWeight(2)
    global x, y, kolor
    x = 300
    y = 25
    kolor = 0

def draw():
    global x, y, kolor
    ellipse(x, y, 40, 40)
    kolor = kolor + 1
    stroke(150 + kolor,0 + kolor,150 - kolor)
    x = x + 1
    y = y + 1
    if y > 300:
        x = x - 2
        kolor = kolor - 2
    if x < 300:
        y = y - 2
def mousePressed():
    exit()
    
# wiem, że ponieważ polecenie if x > 575 przypisuje x podane wartości tylko wtedy
# kiedy spełnia warunek, koło nie może zmienić kierunku na stałe, jednak nie wiem
# jak temu zaradzić

# dodać drugi warunek na y oba razem już będą się różniły
# w tym zadaniu ważna byłą zmiana kolorów i powtórzenie kolekcji
# 0,5pkt w obecnym stanie
        
#zmieniłem warunki x i y, teraz obiekt porusza się prawidłowo, dodałem zmianę kolorów
