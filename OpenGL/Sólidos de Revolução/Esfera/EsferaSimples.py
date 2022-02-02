from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
from random import *
from numpy import *
 
teta0 = (-math.pi)/2
tetaF = (math.pi)/2
phi0 = 0
phiF = 2*math.pi
r = 10
dphi = math.pi/10
dteta = math.pi/10

def Px(teta):    
    return r*cos(teta)

def Py(teta):
    return r*sin(teta)

def Qx(r2, phi):
    return r2*cos(phi)

def Qz(r2, phi):
    return r2*sin(phi)


def desenho():
    teta = teta0
    phi = phi0
    glBegin(GL_LINES)
    while(tetaF > teta):
        phi = phi0
        while(phiF > phi):
            P = (Qx(Px(teta), phi), Py(teta), Qz(Px(teta), phi))
            Q = (Qx(Px(teta), phi + dphi), Py(teta), Qz(Px(teta), phi + dphi))
            R = (Qx(Px(teta + dteta), phi), Py(teta + dteta), Qz(Px(teta + dteta), phi))
            S = (Qx(Px(teta + dteta), phi + dphi), Py(teta + dteta), Qz(Px(teta + dteta), phi + dphi))
            
            glVertex3fv(P)
            glVertex3fv(R)
            glVertex3fv(R)
            glVertex3fv(S)
            glVertex3fv(P)
            glVertex3fv(Q)
            glVertex3fv(R)
            glVertex3fv(Q)
            glVertex3fv(Q)
            glVertex3fv(S)


            phi += dphi
        teta += dteta
    glEnd()


def esf():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,0,1,0)
    desenho()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Esfera")
    glutDisplayFunc(esf)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.,0.,0.,1.)
    gluPerspective(80,1000.0/800.0,0.1,50.0)
    glTranslatef(0.0,0.0,-20)
    glutTimerFunc(50,timer,1)
    glutMainLoop()

main()
