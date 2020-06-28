class Kwadrat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class KolorowyKwadrat(Kwadrat):
    def sketchKolorowy(self, x, y): # po co przekazywa kolor, skoro go nie wykorzystujesz, tylko nadajesz randomowy?
         fill(random(255), 0, 0) # wypadałoby później przywracać ten kolor, bo w obecej implementacji wszystko narysowane po tym kwadracie będzie w tym kolorze
         Kwadrat.sketch(self, x, y) # wystarczy ras narysować ten kwadrat, nie trzy...
    
def setup():
    size(500, 500)
    background(150,50,200)
    malyKolorowyKwadrat = KolorowyKwadrat(30.0) 
    malyKolorowyKwadrat.sketchKolorowy(random(225), 125) 
    malyKolorowyKwadrat.sketchKolorowy(random(143),268) 
    duzyKolorowyKwadrat = KolorowyKwadrat(120.0)
    duzyKolorowyKwadrat.sketchKolorowy(random(275), 36)
    duzyKolorowyKwadrat.sketch(random(250), 300)
    
# 1,5pkt
