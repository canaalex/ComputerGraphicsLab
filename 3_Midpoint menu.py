from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
n=1

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-80.0,80.0,-80.0,80.0)

def setpixel(xn,yn):
    glBegin(GL_POINTS)
    glVertex2f(xn,yn)
    glEnd()
    glFlush()

def midpoint():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,0.0)        
    glPointSize(5.0)
    r=float(input("Enter the radius"))
    xc=float(input("Enter the center xc coordinate:"))
    yc=float(input("Enter the center yc coordinate:"))
    x=0
    y=r
    setpixel(x+xc,y+yc)
    setpixel(-x+xc,y+yc)
    setpixel(-x+xc,-y+yc)
    setpixel(x+xc,-y+yc)
    setpixel(y+xc,x+yc)
    setpixel(y+xc,-x+yc)
    setpixel(-y+xc,-x+yc)
    setpixel(-y+xc,x+yc) 
    p=5/4-r
    while x<y:
       x+=0.1
       if p<0:
          p=p+2*x+1
       else:
          y-=0.1
          p=p+2*(x-y)+1
       setpixel(x+xc,y+yc)
       setpixel(x+xc,-y+yc)
       setpixel(-x+xc,y+yc)
       setpixel(-x+xc,-y+yc)  
      
    main(n=1)  

def polar():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)        
    glPointSize(5.0)
    r=float(input("Enter the radius"))
    xc=float(input("Enter the center xc coordinate:"))
    yc=float(input("Enter the center yc coordinate:"))
    t=0
    while t<=2*math.pi:
       x=xc+r*math.cos(t)
       y=yc+r*math.sin(t)
       setpixel(x+xc,y+yc)
       setpixel(-x+xc,y+yc)
       setpixel(-x+xc,-y+yc)
       setpixel(x+xc,-y+yc)
       
       t+=1/r
    main(n=1)                   

def nonpolar():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)        
    glPointSize(5.0)
    r=float(input("Enter the radius"))
    xc=float(input("Enter the center xc coordinate:"))
    yc=float(input("Enter the center yc coordinate:"))
    x=xc-r
    while x<=xc+r:
       y=math.sqrt(math.pow(r,2)-math.pow(xc-x,2))
       setpixel(x+xc,y+yc)
       setpixel(x+xc,-y+yc)
       setpixel(-x+xc,y+yc)
       setpixel(-x+xc,-y+yc)   
       x+=1
    main(n=1)   

def main(n):
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    while (n==1):
         print("\n1.Midpoint Circle Drawing Algorithm\n2.Polar Circle Genereation Algorithm\n3.Non-Polar Circle Genereation Algorithm\n4.Exit")
         ch=int(input("Enter Your choice"))
         if ch==1:
            glutCreateWindow("Midpoint Algorithm") 
            init()
            glutDisplayFunc(midpoint) 
            glutMainLoop()

         elif ch==2:
            glutCreateWindow("Polar") 
            init()
            glutDisplayFunc(polar)
            glutMainLoop()

         elif ch==3:
            glutCreateWindow("Non-polar") 
            init()
            glutDisplayFunc(nonpolar)
            glutMainLoop()

         else:
            print("End of the program")
            n=0
            glutLeaveMainLoop()
main(n)