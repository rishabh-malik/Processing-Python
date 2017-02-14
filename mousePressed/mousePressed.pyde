y = 100
def setup():
  size(640, 360) 
  stroke(255)   
  frameRate(30)
  noLoop()



def draw():
    background(0)  
    y =y-1
    if (y < 0): 
        y = height 
    line(0, y, width, y);  

def mousePressed():
    loop()