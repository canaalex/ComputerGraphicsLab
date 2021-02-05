from OpenGL.GL import *
from OpenGL.GLU import *     
from OpenGL.GLUT import *    
import sys
import math
n=1 

def init():
    glClearColor(0.0,0.0,0.0,1.0)  
    gluOrtho2D(-15.0,15.0,-15.0,15.0) 

def setpixel(x1,y1,x2,y2,x3,y3):
    glBegin(GL_LINES)
    glVertex2i(x1,y1)
    glVertex2i(x2,y2)
    glVertex2i(x2,y2)
    glVertex2i(x3,y3)
    glVertex2i(x3,y3)
    glVertex2i(x1,y1)
    glEnd()
    glFlush() 

def axes():
    glClear(GL_COLOR_BUFFER_BIT)  
    glColor3f(0.0,1.0,1.0)        
    glPointSize(10.0)             
    x1=-15
    x2=15
    y=0
    glBegin(GL_LINES)
    glVertex2i(x1,y) 
    glVertex2i(x2,y)   
    glEnd()   
    glFlush()                                 
    x=0
    y1=-15
    y2=15
    glBegin(GL_LINES)
    glVertex2i(x,y1) 
    glVertex2i(x,y2)
    glEnd()
    glFlush()   

def translation():
    axes()  
    glColor3f(1.0,0.0,0.0)        
    print("Enter the coordinates of the triangle:-")
    x1=int(input("Enter x1:"))
    y1=int(input("Enter y1:"))
    x2=int(input("Enter x2:"))
    y2=int(input("Enter y2:"))
    x3=int(input("Enter x3:"))
    y3=int(input("Enter y3:"))
    setpixel(x1,y1,x2,y2,x3,y3) 
    glColor3f(0.0,0.0,1.0)        
    print("\nEnter the translating factor:")
    tx=int(input("Enter tx:"))
    ty=int(input("Enter ty:"))
    setpixel(x1+tx,y1+ty,x2+tx,y2+ty,x3+tx,y3+ty)   
    main(1)         

def rotation():
    axes()  
    glColor3f(1.0,0.0,0.0)        
    print("Enter the coordinates of the triangle:-")
    x1=int(input("Enter x1:"))
    y1=int(input("Enter y1:"))
    x2=int(input("Enter x2:"))
    y2=int(input("Enter y2:"))
    x3=int(input("Enter x3:"))
    y3=int(input("Enter y3:"))
    setpixel(x1,y1,x2,y2,x3,y3) 
    glColor3f(0.0,0.0,1.0)        
    print("\nRotation about origin")
    t=int(input("Enter the angle of rotation"))
    setpixel(int(x1*math.cos(t)-y1*math.sin(t)),int(x1*math.sin(t)+y1*math.cos(t)),int(x2*math.cos(t)-y2*math.sin(t)),int(x2*math.sin(t)+y2*math.cos(t)),int(x3*math.cos(t)-y3*math.sin(t)),int(x3*math.sin(t)+y3*math.cos(t)))  
    main(1)         

def scaling():
    axes()  
    glColor3f(1.0,0.0,0.0)        
    print("Enter the coordinates of the triangle:-")
    x1=int(input("Enter x1:"))
    y1=int(input("Enter y1:"))
    x2=int(input("Enter x2:"))
    y2=int(input("Enter y2:"))
    x3=int(input("Enter x3:"))
    y3=int(input("Enter y3:"))
    setpixel(x1,y1,x2,y2,x3,y3) 
    glColor3f(0.0,0.0,1.0)        
    print("\nScaling about origin\nEnter the scaling factor:")
    sx=int(input("Enter sx:"))
    sy=int(input("Enter sy:"))
    setpixel(x1*sx,y1*sy,x2*sx,y2*sy,x3*sx,y3*sy)  
    main(1)         
          
def reflection():
    axes()  
    glColor3f(1.0,0.0,0.0)        
    print("Enter the coordinates of the triangle:-")
    x1=int(input("Enter x1:"))
    y1=int(input("Enter y1:"))
    x2=int(input("Enter x2:"))
    y2=int(input("Enter y2:"))
    x3=int(input("Enter x3:"))
    y3=int(input("Enter y3:"))
    setpixel(x1,y1,x2,y2,x3,y3) 
    glColor3f(0.0,0.0,1.0)        
    print("\n1.About xaxis\n2.About yaxis\n3.About origin")
    ch=int(input("Enter your choice"))
    if ch==1:
       setpixel(x1,-y1,x2,-y2,x3,-y3)  
    elif ch==2:
       setpixel(-x1,y1,-x2,y2,-x3,y3) 
    else:
       setpixel(-x1,-y1,-x2,-y2,-x3,-y3)  
    main(1)         

def main(n):
    glutInit(sys.argv)           
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)   
    glutInitWindowSize(500,500)    
    glutInitWindowPosition(50,50)  
    while (n==1):
         print("\n1.Translation\n2.Rotation\n3.Scaling\n4.Reflection\n5.Exit")
         ch=int(input("Enter your choice")) 
         if ch==1:
            glutCreateWindow("Translation") 
            init()
            glutDisplayFunc(translation) 
            glutMainLoop()

         elif ch==2:
            glutCreateWindow("Rotation") 
            init()
            glutDisplayFunc(rotation)
            glutMainLoop()

         elif ch==3:
            glutCreateWindow("Scaling") 
            init()
            glutDisplayFunc(scaling)
            glutMainLoop()

         elif ch==4:
            glutCreateWindow("Reflection") 
            init()
            glutDisplayFunc(reflection)
            glutMainLoop()

         else:
            print("End of the program")
            n=0
            glutLeaveMainLoop()
main(n)
