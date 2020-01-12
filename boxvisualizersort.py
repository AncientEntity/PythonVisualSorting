import time, random, pygame, math

windowSize = 500
arraySize = 500
delayPerItem = 0

pygame.init()
screen = pygame.display.set_mode((windowSize,windowSize))

unsorted = []
for i in range(arraySize):
    unsorted.append(random.randint(0,255))
print(unsorted)

amountPerRow = math.floor(math.sqrt(len(unsorted)))
cellSize = windowSize // amountPerRow

def UpdateVisualize(sort):
    screen.fill((255,255,255))
    for x in range(amountPerRow):
        for y in range(amountPerRow):
            pygame.draw.rect(screen,(sort[x*y],sort[x*y],sort[x*y]),(x*cellSize,y*cellSize,cellSize,cellSize))
    pygame.display.update()


def DoSort(toBeSorted):
    hasChanged = False
    keepSorting = True
    while(keepSorting):
        hasChanged = False
        for i in range(len(toBeSorted)-1):
            if(toBeSorted[i+1] > toBeSorted[i]):
                temp = toBeSorted[i+1]
                toBeSorted[i+1] = toBeSorted[i]
                toBeSorted[i] = temp
                hasChanged = True
        time.sleep(delayPerItem)
        #print(toBeSorted)
        if(hasChanged == False):
            keepSorting = False
        UpdateVisualize(toBeSorted)
    return toBeSorted


print("\n\n\n")
done = DoSort(unsorted)
print(done)

time.sleep(5)

