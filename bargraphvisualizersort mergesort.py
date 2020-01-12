import time, random, pygame, math, webbrowser

windowSize = 800
arraySize = 50000
delayPerItem = 0.0
widthMultiplier = 2

pygame.init()
screen = pygame.display.set_mode((windowSize*widthMultiplier,windowSize))

unsorted = []
for i in range(arraySize):
    unsorted.append(random.randint(1,windowSize))
print("List creation done")

#amountPerRow = math.floor(math.sqrt(len(unsorted)))
cellSize = windowSize*widthMultiplier // len(unsorted)
if(cellSize < 1):
    cellSize = 1


def UpdateVisualize(sort):
    screen.fill((0,0,0))
    count = 0
    toDo = []
    toDo = ReturnSingulars(sort)
    #print(toDo)
    #print("size: "+str(len(toDo)))
    
    for i in toDo:
        if(count*cellSize > windowSize*widthMultiplier):
            break
        pygame.draw.rect(screen,(50,50,200),(count*cellSize,windowSize-i,cellSize,i))
        count+=1
    pygame.display.update()

def ReturnSingulars(full):
    good = []
    for element in full:
        if(isinstance(element,list) == False):
            good.append(element)
        else:
            singles = ReturnSingulars(element)
            for s in singles:
                good.append(s)
    return good

def BreakDownList(toBeBroken):
    aftermath = []
    pos = 0
    while pos < len(toBeBroken)-1:
        if(toBeBroken[pos] <= toBeBroken[pos+1]):
            aftermath.append([toBeBroken[pos],toBeBroken[pos+1]])
        else:
            aftermath.append([toBeBroken[pos+1],toBeBroken[pos]])
        pos+=2
    return aftermath

def DoSort(toBeSorted):
    timeStarted = time.time()
    hasChanged = False
    #keepSorting = True
    #lastOne = 0
    #print(toBeSorted) 
    toBeSorted = BreakDownList(toBeSorted)
    #print(ReturnSingulars(toBeSorted))
    while(len(toBeSorted)>1):
        i = 0
        while i < len(toBeSorted)-1:
            one = ReturnSingulars(toBeSorted[i])
            two = ReturnSingulars(toBeSorted[i+1])
            out = []
            while len(one) > 0 and len(two) > 0:
                if(len(two) > 0 and one[0] <= two[0]):
                   out.append(one[0])
                   one.pop(0)
                if(len(one) > 0 and two[0] <= one[0]):
                   out.append(two[0])
                   two.pop(0)
                #UpdateVisualize(toBeSorted)
            for p in one:
                out.append(p)
            for j in two:
                out.append(j)

            #print(i)
            toBeSorted.pop(i)
            toBeSorted[i] = out
            
            i += 2
            time.sleep(delayPerItem)
            #UpdateVisualize(toBeSorted)
        #print(toBeSorted)
        UpdateVisualize(toBeSorted)
    toBeSorted = toBeSorted[0]
    print("Took: "+str(time.time()-timeStarted)+"s")
    return toBeSorted


print("\n\n\n")
done = DoSort(unsorted)
print(done)



#webbrowser.open_new("https://www.youtube.com/watch?v=EPX5IBbfmEQ")

time.sleep(5)

