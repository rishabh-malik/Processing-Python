def setup():
  size(640, 360)

def draw(): 
  stroke(255)
  if mousePressed == 1:
    line(mouseX, mouseY, pmouseX, pmouseY)
  