import time, random, pygame, math

windowSize = 800
arraySize = 800
delayPerItem = 0
widthMultiplier = 2


pygame.init()
screen = pygame.display.set_mode((windowSize*widthMultiplier,windowSize))

unsorted = []
for i in range(arraySize):
    unsorted.append(random.randint(1,windowSize))
print(unsorted)


#amountPerRow = math.floor(math.sqrt(len(unsorted)))
cellSize = windowSize*widthMultiplier // len(unsorted)
if(cellSize < 1):
    cellSize = 1

def UpdateVisualize(sort):
    screen.fill((0,0,0))
    count = 0
    for i in sort:
        pygame.draw.rect(screen,(50,50,200),(count*cellSize,windowSize-i,cellSize,i))
        count+=1
    pygame.display.update()

def DoSort(toBeSorted):
    timeStarted = time.time()
    hasChanged = False
    keepSorting = True
    #lastOne = 0
    while(keepSorting):
        hasChanged = False
        for i in range(len(toBeSorted)-1):
            if(toBeSorted[i+1] > toBeSorted[i]):
                temp = toBeSorted[i+1]
                toBeSorted[i+1] = toBeSorted[i]
                toBeSorted[i] = temp
                hasChanged = True
                #break
        #UpdateVisualize(toBeSorted)
        for j in range(len(toBeSorted)-1):
            i = len(toBeSorted)-1-j
            if(toBeSorted[i-1] < toBeSorted[i]):
                temp = toBeSorted[i-1]
                toBeSorted[i-1] = toBeSorted[i]
                toBeSorted[i] = temp
                hasChanged = True
                #break
        UpdateVisualize(toBeSorted)
        time.sleep(delayPerItem)
        #print(toBeSorted)
        if(hasChanged == False):
            keepSorting = False
    print("Took: "+str(time.time()-timeStarted)+"s")
    return toBeSorted


print("\n\n\n")
done = DoSort(unsorted)
print(done)

time.sleep(5)

