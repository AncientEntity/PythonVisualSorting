import time, random, pygame, math

windowSize = 800
arraySize = 800
delayPerItem = 0.0
widthMultiplier = 2
maxValueMultiplier = 1

pygame.init()
screen = pygame.display.set_mode((windowSize*widthMultiplier,windowSize))

unsorted = []
for i in range(arraySize):
    unsorted.append(random.randint(1,windowSize*maxValueMultiplier))
#print(unsorted)

#amountPerRow = math.floor(math.sqrt(len(unsorted)))
cellSize = windowSize*widthMultiplier // len(unsorted)
if(cellSize < 1):
    cellSize = 1
maxValueInList = max(unsorted)

def UpdateVisualize(sort):
    screen.fill((0,0,0))
    count = 0
    for i in sort:
        if(count*cellSize > windowSize*widthMultiplier):
            break
        pygame.draw.rect(screen,(50,50,200),(count*cellSize,windowSize-(i/maxValueInList*windowSize),cellSize,(i/maxValueInList*windowSize)))
        count+=1
    pygame.display.update()

def GetStringVersion(i,m):
    return ("0"*(m-len(str(i))))+str(i)

def DoSort(toBeSorted):
    timeStarted = time.time()
    hasChanged = False
    keepSorting = True
    maxValue = max(toBeSorted)
    maxLength = len(str(maxValue))
    UpdateVisualize(toBeSorted)

    #for i in range(len(toBeSorted)):
    #    print(GetStringVersion(toBeSorted[i],maxLength))
    
    for digit in range(maxLength):
        cur = maxLength - digit-1
        print(cur)
        nextList = [[],[],[],[],[],[],[],[],[],[]]
        for element in toBeSorted:
            strV = GetStringVersion(element,maxLength)
            nextList[int(strV[cur])].append(element)

        toBeSorted = []
        for microList in nextList:
            for element in microList:
                toBeSorted.append(element)
            UpdateVisualize(toBeSorted)
            time.sleep(delayPerItem)
        
        UpdateVisualize(toBeSorted)
    print("Took: "+str(time.time()-timeStarted)+"s")
    return toBeSorted


print("\n\n\n")
done = DoSort(unsorted)
#print(done)

time.sleep(5)

