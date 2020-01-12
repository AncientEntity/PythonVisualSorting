import time, random, pygame, math

windowSize = 600
arraySize = 600
delayPerItem = 0
widthMultiplier = 2

pygame.init()
screen = pygame.display.set_mode((windowSize*widthMultiplier,windowSize))

unsorted = []


for i in range(arraySize):
    unsorted.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
print(unsorted)

#amountPerRow = math.floor(math.sqrt(len(unsorted)))
cellSize = windowSize*widthMultiplier // len(unsorted)

def UpdateVisualize(sort):
    screen.fill((0,0,0))
    count = 0
    for i in sort:
        pygame.draw.rect(screen,i,(count*cellSize,0,cellSize,windowSize))
        count+=1
    pygame.display.update()

def DoSort(toBeSorted):
    hasChanged = False
    keepSorting = True
    #lastOne = 0
    while(keepSorting):
        hasChanged = False
        for i in range(len(toBeSorted)-1):
            if(toBeSorted[i+1][0] > toBeSorted[i][0]):
                temp = toBeSorted[i+1]
                toBeSorted[i+1] = toBeSorted[i]
                toBeSorted[i] = temp
                hasChanged = True
                #break
            elif(toBeSorted[i+1][0] == toBeSorted[i][0] and toBeSorted[i+1][1] > toBeSorted[i][1]):
                temp = toBeSorted[i+1]
                toBeSorted[i+1] = toBeSorted[i]
                toBeSorted[i] = temp
                hasChanged = True
                #break
            elif(toBeSorted[i+1][0] == toBeSorted[i][0] and toBeSorted[i+1][1] == toBeSorted[i][1] and toBeSorted[i+1][2] > toBeSorted[i][2]):
                temp = toBeSorted[i+1]
                toBeSorted[i+1] = toBeSorted[i]
                toBeSorted[i] = temp
                hasChanged = True
                #break
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

