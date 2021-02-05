from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
def init():
 glClearColor(0.0,0.0,0.0,1.0)
 gluOrtho2D(-80.0,80.0,-80.0,80.0)
 glPointSize(5.0)
 glColor3f(0.0,1.0,1.0)

def setpixel(xn,yn):
 glBegin(GL_POINTS)
 glVertex2f(xn,yn)
 glEnd()
 glFlush()

def readinput():
 global a,b,xc,yc
 a=float(input("Enter the length of semi major axis:"))
 b=float(input("Enter the length of semi minor axis:"))
 xc=float(input("Enter the center xc coordinate:"))
 yc=float(input("Enter the center yc coordinate:"))

def polar():
 readinput()
 t=0
 end=(22/7)/2
 while t<end:
      x=(a*math.cos(t))
      y=(b*math.sin(t))
      setpixel(xc+x,yc+y)
      setpixel(xc-x,yc+y)
      setpixel(xc-x,yc-y)
      setpixel(xc+x,yc-y)
      t+=0.001
 glFlush()
 
 

def nonpolar():
 readinput()
 x=0
 y=0
 while x<=a:
     y=math.sqrt(math.pow(a*b,2)-math.pow(x*b,2))/a
     setpixel(xc+x,yc+y)
     setpixel(xc-x,yc+y)
     setpixel(xc-x,yc-y)
     setpixel(xc+x,yc-y)
     x=x+0.001
 glFlush()


def DisplayPolar():
 glClear(GL_COLOR_BUFFER_BIT)
 glutSwapBuffers()
 polar()

def DisplayNonPolar():
 glClear(GL_COLOR_BUFFER_BIT)
 glutSwapBuffers()
 nonpolar()

def main():
 glutInit(sys.argv)
 glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
 glutInitWindowSize(500,500)
 glutInitWindowPosition(100,100)
 print("\n1.Polar Ellipse Generation Algorithm\n 2.Non-Polar Ellipse Generation Algorithm\n 3. or Exit")

 ch=int(input("Enter Your choice:"))
 if ch==1:
     glutCreateWindow("Polar Ellipse Algorithm")
     glutDisplayFunc(DisplayPolar)
 
 
 elif ch==2:
     glutCreateWindow("Non-polar Ellipse Algorithm")
     glutDisplayFunc(DisplayNonPolar)
 
 
 elif ch==3:
     exit()
 
 else:
      print("Invalid Choice")
      exit()

 
 init()
 glutMainLoop()
main()