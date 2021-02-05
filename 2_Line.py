from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
print('package Import Successful') 
w, h = 400, 400 #height and width of screen 
def float_range(start,stop,step=0.1):
    x=start
    while x<=stop: 
         yield x 
         x=x+step 

    # function to pass floating points 




def showHorizontal():# function of horizontal line 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity() 
    glColor3f(1.0,0.5,0.0)
    glPointSize(10.0) 
    glBegin(GL_POINTS)
    fr=float_range(x1Value,x2Value)  
    for i in fr: 
        glVertex2f(i,yValue)
    glVertex2f(x1Value, yValue) 
    glEnd() 
    glFlush() 







 

def showVertical():# function of vertical line 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity() 
    glColor3f(0.439216,0.576471,0.858824) 
    glPointSize(10.0) 
    glBegin(GL_POINTS) 
    fr=float_range(y1Value,y2Value) 
    for i in fr: 
        glVertex2f(xValue,i) 
    glVertex2f(xValue, y1Value) 
    glEnd() 
    glutSwapBuffers() 









def showDiagonal():# function of diagonal line 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    glColor3f(1.0,0.43,0.78) 
    glPointSize(10.0)
    glBegin(GL_POINTS) 
    fr=float_range(Value1,Value2) 
    for i in fr: 
        glVertex2f(i,i) 
    glEnd() 
    glutSwapBuffers() 
 





#Listing options 
option = int(input(' List \n 1)Enter 1 for horizontal line\n 2)Enter 2 for vertical line \n 3)Enter 3 for diagonal line : ')) 
if option == 1: 
    print('Values selected for horizontal line') 
    x1Value = float(input('Enter x1 value : '))/100 
    x2Value = float(input('Enter x2 value : '))/100 
    yValue = float(input('Enter y value : '))/100 
    glutInit() 
    glutInitDisplayMode(GLUT_RGB) 
    glutInitWindowSize(w, h) 
    glutInitWindowPosition(100,100) 
    glutCreateWindow('Horizontal line') 
    glutDisplayFunc(showHorizontal) 
    glutIdleFunc(showHorizontal) 
    glutMainLoop() 

if option == 2: 
    print('Values selected for vertical line') 
    xValue = float(input('Enter x value : '))/100
    y1Value = float(input('Enter y1 value : '))/100 
    y2Value = float(input('Enter y2 value : '))/100 
    glutInit() 
    glutInitDisplayMode(GLUT_RGB) 
    glutInitWindowSize(w, h) 
    glutInitWindowPosition(100,100) 
    glutCreateWindow('Vertical line') 
    glutDisplayFunc(showVertical) 
    glutIdleFunc(showVertical) 
    glutMainLoop() 

if option == 3: 
    print('Values selected for diagonal line') 
    Value1 = float(input('Enter value1 : '))/100 
    Value2 = float(input('Enter value2 : '))/100 
    glutInit() 
    glutInitDisplayMode(GLUT_RGB) 
    glutInitWindowSize(w, h) 
    glutInitWindowPosition(100,100) 
    glutCreateWindow('Diagonal line') 
    glutDisplayFunc(showDiagonal) 
    glutIdleFunc(showDiagonal) 
    glutMainLoop() 

else: 
    print('Invalid option\n Please select the right option')
    

