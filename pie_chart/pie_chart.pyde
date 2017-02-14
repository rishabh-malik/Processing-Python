import math
angles = { 30, 10, 45, 35, 60, 38, 75, 67 }


def setup(): 
  size(640, 360)
  noStroke()
  noLoop()
  
def draw():
  background(100)
  pieChart(300, angles)


def pieChart(diameter,data):
  lastAngle = 0
  for i in range(0,len(data),1): 
    gray = map(i, 0,len(data), 0, 255)
    fill(gray)
    arc(width/2, height/2, diameter, diameter, lastAngle, lastAngle+math.radians(angles[i]))
    lastAngle += radians(angles[i])
  