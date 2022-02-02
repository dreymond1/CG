from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

from math import *
import math
import random

dist = 2

side_count = 6

window = 0
	
height = 1.8

side_rads_size = (2*math.pi)/side_count

down_radius = 1.3
up_radius = 0.5
down_vertices = []
up_vertices = []


currentRotationX = currentRotationY = currentRotationZ = 0.0
offsetRotationX = 0.07
offsetRotationY = 0.05
offsetRotationZ = 0.02

def InitGL(Width, Height):             
	glClearColor(0.9, 0.8, 0.0, 0.0) 
	glClearDepth(1.0)
	glDepthFunc(GL_LESS)               
	glEnable(GL_DEPTH_TEST)            
	glShadeModel(GL_SMOOTH)            
	glMatrixMode(GL_PROJECTION)
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)
	glColor3fv((1,1,0))

def ReSizeGLScene(Width, Height):
	if Height == 0:                        
		Height = 1
	glViewport(0, 0, Width, Height)      
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
	global currentRotationX, currentRotationY, currentRotationZ, down_vertices, up_vertices

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
	glLoadIdentity()                   
	glClearColor(0.8,0.1,0.5,1.0)            
	glTranslatef(0.0,0.0,-5.0)
	glRotatef(currentRotationX,1.0,0.0,0.0)
	glRotatef(currentRotationY,0.0,1.0,0.0)
	glRotatef(currentRotationZ,0.0,0.0,1.0)
	glBegin(GL_POLYGON)

	for i in range(0,side_count):
		x = down_radius * math.cos(i*side_rads_size)
		y = down_radius * math.sin(i*side_rads_size)
		glTexCoord2f(math.cos(i), math.sin(i))
		down_vertices += [ (x,y) ]
		glVertex3f(x,y,0.0)
	glEnd()

	glBegin(GL_POLYGON)
	for i in range(0,side_count):
		x = up_radius * math.cos(i*side_rads_size)
		y = up_radius * math.sin(i*side_rads_size)
		glTexCoord2f(math.cos(i), math.sin(i))
		up_vertices += [ (x,y) ]
		glVertex3f(x,y,height)
	glEnd()

	glBegin(GL_QUADS)
	for i in range(0,side_count):
		glTexCoord2f(0.0, 1.0); glVertex3f(down_vertices[i][0],down_vertices[i][1],0.0)
		glTexCoord2f(0.0, 0.0); glVertex3f(up_vertices[i][0],up_vertices[i][1],height)
		glTexCoord2f(1.0, 0.0); glVertex3f(up_vertices[(i+1)%side_count][0],up_vertices[(i+1)%side_count][1],height)
		glTexCoord2f(1.0, 1.0); glVertex3f(down_vertices[(i+1)%side_count][0],down_vertices[(i+1)%side_count][1],0.0)
	glEnd()
    
	currentRotationX = currentRotationX + offsetRotationX
	currentRotationY = currentRotationY + offsetRotationY
	currentRotationZ = currentRotationZ + offsetRotationZ

	glutSwapBuffers()


def main():
	global window
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowSize(640, 480)
	glutInitWindowPosition(0, 0)
	window = glutCreateWindow("Tronco de Piramide")
	glutDisplayFunc(DrawGLScene)
	glutIdleFunc(DrawGLScene)
	glutReshapeFunc(ReSizeGLScene)
	
	InitGL(640, 480)

	glutMainLoop()


main()
