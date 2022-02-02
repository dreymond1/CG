from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

def Cilindro(n,r,h):
    
    glBegin(GL_POLYGON)
    glColor3f(0,1,1)
    posicao = cilindro(n,r)    
    for i in range(n):
            glVertex3f(posicao[1][i][0],posicao[1][i][1],posicao[1][i][2])
    glEnd()

    glBegin(GL_QUAD_STRIP)
    glColor3f(1,0,1)
    for i in range(n):
            glVertex3f(posicao[0][i][0],posicao[0][i][1],posicao[0][i][2])
            glVertex3f(posicao[0][i][0],posicao[0][i][1],posicao[0][i][2]+h)
    glEnd()

    glBegin(GL_POLYGON)
    for i in range(n):
            glColor3f(1,1,1)
            glVertex3f(posicao[1][i][0],posicao[1][i][1],posicao[1][i][2]+h)
    glEnd()

def cilindro(n,r,h=2):
    base = poligono(n,r)
    lados = poligono(n,r)
    return [lados, base]

def cil():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,0,0)
    Cilindro(n=50,r=1,h=2)
    glutSwapBuffers()
 
def poligono(n,r):
    pontos = []
    alpha = (2*math.pi)/n
    for i in range(0,n):
        px = r * math.cos(i*alpha)
        py = r * math.sin(i*alpha)
        pz = 0
        pontos.append([px,py,pz])
    return pontos

def timer(i):
    glutPostRedisplay()
    glutTimerFunc((1000/60),timer,1)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Cilindro")
    glutDisplayFunc(cil)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.,0.,0.,1.)
    gluPerspective(45,800.0/600.0,0.1,50.0)
    glTranslatef(0.0,0.0,-10)
    glutTimerFunc(50,timer,1)
    glutMainLoop()

main()
