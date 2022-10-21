import pygame, time ,random

pygame.init()

mazeSize = (100,100)

screen = pygame.display.set_mode((mazeSize[0]*5,mazeSize[1]*5))

PATH = 1
WALL = 0
UNDEFINED = -1
ENTRANCE = 2
EXIT = 3

maze = []

#create undefined maze
for x in range(mazeSize[0]):
    maze.append([])
    for y in range(mazeSize[1]):
        maze[x].append(-1)
maze[0][0] = ENTRANCE
maze[mazeSize[0]-1][mazeSize[1]-1] = EXIT

def FindPath(maze,curPos):


def DrawMaze(maze,size):
    global screen
    screen.fill((0,0,0))
    for x in range(size[0]):
        for y in range(size[1]):
            if(maze[x][y] == PATH):
                pygame.draw.rect(screen,(255,255,255),(x*5,y*5,5,5))

    pygame.display.update()

DrawMaze(maze,mazeSize)