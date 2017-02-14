


def setup():
  y = 100
  size(640, 360) 
  stroke(255)   
  frameRate(30)



def draw():
    background(0)  
    y--
    if (y < 0): 
        y = height 
    line(0, y, width, y);  