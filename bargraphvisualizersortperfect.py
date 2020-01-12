import time, random, pygame, math

windowSize = 800
arraySize = 800
delayPerItem = 0
widthMultiplier = 2

pygame.init()
screen = pygame.display.set_mode((windowSize*widthMultiplier,windowSize))

unsorted = []
temp = list(range(arraySize))
for i in range(arraySize):
    r = random.randint(0,len(temp)-1)
    if(random.randint(0,1) == 1):
        unsorted.insert(0,temp[r])
    else:
        unsorted.insert(len(unsorted),temp[r])
    temp.remove(temp[r])
print(unsorted)

#amountPerRow = math.floor(math.sqrt(len(unsorted)))
cellSize = windowSize*widthMultiplier // len(unsorted)

def UpdateVisualize(sort):
    screen.fill((0,0,0))
    count = 0
    for i in sort:
        pygame.draw.rect(screen,(50,50,200),(count*cellSize,windowSize-i,cellSize,i))
        count+=1
    pygame.display.update()

def DoSort(toBeSorted):
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

