PImage img;
void setup()
{
  size(640,360);
  img=loadImage("pic.jpg");
}
void draw()
{
  image(img,0,0);
}