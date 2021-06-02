from typing import List
class City:
    def __init__(self, xDirection: int, yDirection: int):
        self.xDirection = xDirection
        self.yDirection = yDirection

class Good:
    coeff:float
    def __init__(self, id:int, weight:int, value:int, xDirection: int, yDirection: int):
        self.id = id
        self.weight = weight
        self.value = value
        self.city = City(xDirection, yDirection)


def floyd_warshall(distance):

    for k in range(10):
        for i in range(10):
            for j in range(10):
                if(distance[i][j] > distance[k][j] + distance[i][k]):
                    P[i][j] = k
                    distance[i][j] = distance[k][j] + distance[i][k]
    

def onTheRoadGoods(good: Good, visitedCities: List[int], counter: int):
    x = good.city.xDirection
    y = good.city.yDirection
    city = P[y][x]
    while city != 0:
        visitedCities.insert(counter, city) 
        x = city
        counter+=1
        city = P[y][x]
    visitedCities.insert(counter, y)

def isVisited(city: int, visitedCities: int, numberOfElements: int):
    for i in range(numberOfElements):
        if(city == visitedCities[i]):
            return True
    return False

def chooseGood(max_weight: int, listOfGoods: List[Good], lastIndex:int):
    for i in range(lastIndex, -1, -1):
        if(max_weight - listOfGoods[i].weight >= 0):
            return i
        else:
            return -1

###def shift(listOfGoods: List[Good], lastIndex:int, deletedIndex:int):





infinity = 1000
cities = [[0, 150, 300, 200, infinity, infinity,infinity,infinity,infinity,infinity],
                      [140, 0, 100, infinity, 200, infinity, infinity, infinity, infinity, infinity],
                      [290, 90, 0, 100, infinity, 400, infinity, infinity, infinity, infinity],
                      [190, infinity, 90, 0, infinity, infinity, 300, infinity, infinity, infinity],
                      [infinity, 190, infinity, infinity, 0, infinity, infinity, 200, infinity, infinity],
                      [infinity, infinity, 390, infinity, infinity, 0, infinity, 250, 300, 100],
                      [infinity, infinity, infinity, 290, infinity, infinity, 0, infinity, infinity, 200],
                      [infinity, infinity, infinity, infinity, 190, 240, infinity, 0, 100, infinity],
                      [infinity, infinity, infinity, infinity, infinity, 290, infinity, 90, 0, infinity],
                      [infinity, infinity, infinity, infinity, infinity, 90, 190, infinity, infinity, 0]]


P = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
distance = cities
print(cities)
floyd_warshall(distance)
print(distance)
print(P)


def getOptimalList(maxWeight:int, numberOfElements:int, listOfGoods: List[Good], optimalList: List[Good]):
    counter = 0
    currentLocation = 0
    optimalCounter = 0
    visitedCities: List[int] = []
    while maxWeight != 0 and numberOfElements != 0:
        lastIndex = numberOfElements - 1 
        for i in range(numberOfElements):
            good = listOfGoods[i]
            if(isVisited(good.city.xDirection, visitedCities, counter)):
                good.coeff = good.value / good.weight
            else:
                good.coeff = (good.value - distance[currentLocation][good.city.xDirection]) / good.weight
        listOfGoods.sort(key = lambda x: x.weight)
        index = chooseGood(maxWeight, listOfGoods, lastIndex)
        if(index>=0):
            maxWeight -= listOfGoods[index].weight
            optimalList.append(listOfGoods[index].id)
            if(not isVisited(listOfGoods[index].city.xDirection, visitedCities, counter)):
                onTheRoadGoods(listOfGoods[index], visitedCities, counter)
                currentLocation = listOfGoods[index].city.xDirection
            listOfGoods.pop(index)
            optimalCounter+=1
        else:
            break
        numberOfElements-=1
    return optimalList

def input_list(listOfGoods, numberOfElements):
    for i in range(numberOfElements):
        weight:int
        value:int
        x:int
        print("Good#", i+1)
        print("Weight: ")
        weight = int(input())
        print("Value: ")
        value = int(input())
        print("City Direction: ")
        x = int(input())
        good = Good(i+1, weight, value, x, 0)
        listOfGoods.append(good)

numberOfElements:int = 0
max_weight:int = 0

print("Number of goods: ")
numberOfElements = int(input())

print("Capacity: ")
max_weight = int(input())
listOfGoods: List[Good] = []
input_list(listOfGoods, numberOfElements)
optimalList: List[Good] = []
optimalList = getOptimalList(max_weight, numberOfElements, listOfGoods, optimalList)
print(optimalList)

    