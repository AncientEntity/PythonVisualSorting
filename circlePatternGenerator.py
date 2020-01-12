import pygame,time,random,math

windowSize = 800
maxCircleSize = windowSize * 0.3
circleCount = windowSize // 2
delay = 0.0

pygame.init()
screen = pygame.display.set_mode((windowSize,windowSize))




screen.fill((255,255,255))
pygame.display.update()

generatedCircles = [] #(x,y,radius)

def Distance(vec1,vec2):
    return math.sqrt(math.pow((vec1[0]-vec2[0]),2)+math.pow((vec1[1]-vec2[1]),2))

#print(Distance([0,0],[5,5]))


def FindValidPosition(circles):
    finding = True
    while finding:
        finding = False
        test = [random.randint(0,windowSize),random.randint(0,windowSize)]
        for c in circles:
            if(Distance((c[0],c[1]),test) < c[2]):
                finding = True
        if(finding == False):
            return test
            
def CheckCollision(circles,cur):
    for c in circles:
        d = Distance((c[0],c[1]),(cur[0],cur[1]))
        if(d - (c[2] + cur[2]) < 0):
            return True
    return False

for j in range(circleCount):
    pos = FindValidPosition(generatedCircles)
    randomColor = [random.randint(60,255),random.randint(60,255),random.randint(60,255)]
    curSize = 2
    keepGoing = True
    while curSize < maxCircleSize and keepGoing == True:
        randomColor[0] -= 1
        randomColor[1] -= 1
        randomColor[2] -= 1
        if(randomColor[0] <= -1):
            randomColor[0] = 0
        if(randomColor[1] <= -1):
            randomColor[1] = 0     
        if(randomColor[2] <= -1):
            randomColor[2] = 0
        #print(randomColor)
        pygame.draw.circle(screen,(randomColor[0],randomColor[1],randomColor[2]),pos,curSize,2)
        pygame.display.update()
        time.sleep(delay)
        curSize += 1
        if(CheckCollision(generatedCircles,(pos[0],pos[1],curSize))):
            break
    generatedCircles.append([pos[0],pos[1],curSize])

